import sys

from models_ia.mlp.handle_trainer import HandlerTrainer, plot_scatter

sys.path.append('/home/marvin/PycharmProjects/IA_CCS/data_handling')

param_grid = {
    'n_layers': [2, 4, 8],
    'n_hidden': [16, 32, 64],
    'lr': [0.001, 0.0001],

}

# results = []
# num_repeat = 5
# epochs = 150
# for n_layers in param_grid['n_layers']:
#     for n_hidden in param_grid['n_hidden']:
#         for lr in param_grid['lr']:
#             for repeat in range(num_repeat):
#                 handle_trainer = HandlerTrainer(n_layers, n_hidden, lr, epochs, repeat)
#                 handle_trainer.set_datas()
#                 handle_trainer.train()
#                 evaluation = handle_trainer.evaluate_model()
#                 results.append(evaluation)
#                 print(f"Treinado com parâmetros: {n_layers, n_hidden}, {lr}, {epochs}")
#                 print(f"Resultados: MSE = {evaluation['mse']:.4f}, MAE = {evaluation['mae']:.4f}")
#
# # Exibir todos os resultados
# for result in results:
#     print(result)


handler_trainer = HandlerTrainer(n_layers=4, n_hidden=32, lr=0.001, epochs=150, num_repeat=5)
handler_trainer.set_datas()
handler_trainer.train()
evaluation = handler_trainer.evaluate_model_val()
plot_scatter(evaluation['predictions'], handler_trainer.y_val)
# Avaliar o modelo no conjunto de teste
# model.eval()
# test_loss = 0.0
# with torch.no_grad():
#     for n in range(x_test.size()[0]):
#         y_hat = model(x_test[n])
#         test_loss += ((y_test[n] - y_hat)**2).item()
# test_loss /= x_test.size()[0]
# print(f'Test Loss: {test_loss:.4f}')
#
# pca = PCA(n_components=2)
# x_reduced = pca.fit_transform(x_normalized)
#
# # Plotar os dados originais e as previsões
# plt.scatter(x_reduced[:, 0], x_reduced[:, 1], c=y, cmap='viridis', label='Dados Originais')
# plt.scatter(x_reduced[:, 0], x_reduced[:, 1], c=model(x_normalized).detach().numpy().flatten(), cmap='coolwarm', label='Previsões', marker='x')
#
# plt.xlabel('Componente Principal 1')
# plt.ylabel('Componente Principal 2')
# plt.legend()
# plt.show()