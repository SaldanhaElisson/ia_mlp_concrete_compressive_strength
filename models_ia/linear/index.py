import sys

from models_ia.linear.handle_trainer import HandlerTrainer  # Altere para o handler do modelo linear

sys.path.append('/home/Documents/development/ia_mlp_concrete_compressive_strength/data_handling')

import torch


param_grid = {
    'lr': [0.001, 0.0001],
    'epochs': [100, 150]
}

results = []

for lr in param_grid['lr']:
    for epochs in param_grid['epochs']:
        handle_trainer = HandlerTrainer(lr, epochs)
        handle_trainer.set_datas()
        handle_trainer.train()
        evaluation = handle_trainer.evaluate_model()
        results.append(evaluation)
        print(f"Treinado com parâmetros: {lr}, {epochs}")
        print(f"Resultados: MSE = {evaluation['mse']:.4f}, MAE = {evaluation['mae']:.4f}")

# Exibir todos os resultados
for result in results:
    print(result)