"""Adaptation and Learning System for Eugene AI"""

import random
from datetime import datetime
from config.settings import ADAPTATION_SETTINGS


class AdaptationSystem:
    """System for continuous learning and adaptation"""

    def __init__(self):
        """Initialize adaptation system"""
        self.settings = ADAPTATION_SETTINGS
        self.population = []
        self.fitness_history = []
        self.generation = 0
        self.best_solution = None
        self.best_fitness = 0

    def initialize_population(self, size=None):
        """Initialize population for genetic algorithm"""
        size = size or self.settings["population_size"]
        self.population = [self._create_individual() for _ in range(size)]

    def _create_individual(self):
        """Create an individual solution"""
        return {
            'genes': [random.random() for _ in range(10)],
            'fitness': 0,
            'age': 0,
        }

    def evaluate_fitness(self, individual, evaluation_function):
        """Evaluate fitness of individual"""
        fitness = evaluation_function(individual['genes'])
        individual['fitness'] = fitness
        return fitness

    def evolve(self, evaluation_function, generations=10):
        """Evolve population over generations"""
        for gen in range(generations):
            # Evaluate population
            for individual in self.population:
                self.evaluate_fitness(individual, evaluation_function)

            # Track best
            best = max(self.population, key=lambda x: x['fitness'])
            if best['fitness'] > self.best_fitness:
                self.best_fitness = best['fitness']
                self.best_solution = best.copy()

            self.fitness_history.append(self.best_fitness)
            self.generation += 1

            # Selection, crossover, mutation
            self.population = self._breed_next_generation()

    def _breed_next_generation(self):
        """Create next generation through breeding"""
        # Sort by fitness
        sorted_pop = sorted(self.population, key=lambda x: x['fitness'], reverse=True)

        # Elite preservation
        elite_size = max(1, len(sorted_pop) // 10)
        new_population = [ind.copy() for ind in sorted_pop[:elite_size]]

        # Breeding
        mutation_rate = self.settings["mutation_rate"]
        while len(new_population) < len(self.population):
            parent1 = random.choice(sorted_pop[:len(sorted_pop)//2])
            parent2 = random.choice(sorted_pop[:len(sorted_pop)//2])

            offspring = self._crossover(parent1, parent2)
            offspring = self._mutate(offspring, mutation_rate)
            new_population.append(offspring)

        return new_population[:len(self.population)]

    def _crossover(self, parent1, parent2):
        """Create offspring through crossover"""
        crossover_point = random.randint(0, len(parent1['genes']))
        offspring_genes = (
            parent1['genes'][:crossover_point] +
            parent2['genes'][crossover_point:]
        )
        return {
            'genes': offspring_genes,
            'fitness': 0,
            'age': 0,
        }

    def _mutate(self, individual, mutation_rate):
        """Apply mutation to individual"""
        for i in range(len(individual['genes'])):
            if random.random() < mutation_rate:
                individual['genes'][i] = random.random()
        return individual

    def get_best_solution(self):
        """Get the best evolved solution"""
        return self.best_solution

    def get_adaptation_stats(self):
        """Get adaptation statistics"""
        return {
            'generation': self.generation,
            'best_fitness': self.best_fitness,
            'population_size': len(self.population),
            'fitness_history': self.fitness_history,
        }

    def __repr__(self):
        return f"AdaptationSystem(Gen: {self.generation}, Best Fitness: {self.best_fitness:.3f})"
