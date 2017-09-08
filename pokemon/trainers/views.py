from django.contrib import messages
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from pokemon.authentication.mixins import LoginMixin

from .forms import TrainerForm, PokemonForm
from .models import Badge, FavoritePokemon, Trainer


class BadgeList(LoginMixin, ListView):
    template_name = 'trainers/badges.html'
    queryset = Badge.objects.annotate(awarded=Count('trainer_badges'))


class PokemonList(LoginMixin, ListView):
    template_name = 'trainers/pokemon.html'
    queryset = FavoritePokemon.objects.select_related('trainer').order_by('-cp')[:100]
    paginate_by = 40


class TrainerCreate(LoginMixin, CreateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'trainers/edit.html'

    def form_valid(self, form):
        trainer = form.save(commit=False)
        trainer.user = self.request.user
        trainer.save()
        return redirect(trainer.url)


class TrainerEdit(LoginMixin, UpdateView):
    model = Trainer
    form_class = TrainerForm
    pokemon_form_class = PokemonForm
    template_name = 'trainers/edit.html'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            messages.warning(
                self.request,
                'You do no have permission to edit this trainer'
            )
            return redirect('trainers')
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Trainer, username__iexact=self.kwargs['username'])

    def get(self, request, username, *args, **kwargs):
        trainer = self.get_object()
        form = self.form_class(instance=trainer)
        pokemon_form = self.pokemon_form_class(instance=trainer)
        return self.render_to_response({
            'form': form,
            'pokemon_form': pokemon_form
        })

    def post(self, request, username, *args, **kwargs):
        trainer = self.get_object()
        form = self.form_class(request.POST, instance=trainer)
        pokemon_form = self.pokemon_form_class(request.POST, instance=trainer)
        if form.is_valid() and pokemon_form.is_valid():
            return self.form_valid(form, pokemon_form)
        return self.render_to_response({
            'form': form,
            'pokemon_form': pokemon_form
        })

    def form_valid(self, form, pokemon_form):
        trainer = form.save()
        if pokemon_form.has_changed():
            pokemon_form.save()
        messages.success(self.request, 'Trainer Stats Updated')
        return redirect(trainer.url)


class TrainerDetail(LoginMixin, DetailView):
    model = Trainer
    template_name = 'trainers/detail.html'

    def get_object(self):
        return get_object_or_404(Trainer, username__iexact=self.kwargs['username'])


class TrainerList(LoginMixin, ListView):
    template_name = 'trainers/index.html'
    queryset = Trainer.objects.prefetch_related('favorite_pokemon').order_by('-xp')
    paginate_by = 40

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated():
            if hasattr(self.request.user, 'trainer'):
                return super().dispatch(request, *args, **kwargs)
            return redirect('trainer-create')
        return redirect('/')
