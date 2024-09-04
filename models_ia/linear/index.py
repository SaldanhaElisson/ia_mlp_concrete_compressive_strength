import sys

from models_ia.linear.handle_trainer import HandlerTrainer, plot_scatter

sys.path.append('/home/Documents/development/ia_mlp_concrete_compressive_strength/data_handling')

param_grid = {
    'lr': [0.001, 0.0001],
    'n_hidden': [16, 32, 64],
    'n_layers': [1],
}

results = []
num_repeat = 5
epochs = 150
#
# for n_hidden in param_grid['n_hidden']:
#     for lr in param_grid['lr']:
#         for repeat in range(num_repeat):
#             handle_trainer = HandlerTrainer(1, n_hidden, lr, epochs, repeat)
#             handle_trainer.set_datas()
#             handle_trainer.train()
#             evaluation = handle_trainer.evaluate_model()
#             results.append(evaluation)
#             print(f"Treinado com parâmetros: {n_hidden}, {lr}, {epochs}")
#             print(f"Resultados: MSE = {evaluation['mse']:.4f}, MAE = {evaluation['mae']:.4f}")
#
# # Exibir todos os resultados
# for result in results:
#     print(result)



handler_trainer = HandlerTrainer(n_layers=1, n_hidden=16, lr=0.001, epochs=150, num_repeat=5)
handler_trainer.set_datas()
handler_trainer.train()
evaluation = handler_trainer.evaluate_model_val()
plot_scatter(evaluation['predictions'], handler_trainer.y_val)