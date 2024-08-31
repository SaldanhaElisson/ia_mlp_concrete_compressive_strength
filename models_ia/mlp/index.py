import sys

from models_ia.mlp.handle_trainer import HandlerTrainer

sys.path.append('/home/marvin/PycharmProjects/IA_CCS/data_handling')

from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import torch


param_grid = {
    'n_layers': [2, 4, 8],
    'n_hidden': [16, 32, 64],
    'lr': [0.001, 0.0001],
    'epochs': [100, 150]
}

results = []

for n_layers in param_grid['n_layers']:
    for n_hidden in param_grid['n_hidden']:
        for lr in param_grid['lr']:
            for epochs in param_grid['epochs']:
                handle_trainer = HandlerTrainer(n_layers, n_hidden, lr, epochs)
                handle_trainer.set_datas()
                handle_trainer.train()
                evaluation = handle_trainer.evaluate_model()
                results.append(evaluation)
                print(f"Treinado com parâmetros: {n_layers, n_hidden}, {lr}, {epochs}")
                print(f"Resultados: MSE = {evaluation['mse']:.4f}, MAE = {evaluation['mae']:.4f}")

# Exibir todos os resultados
for result in results:
    print(result)




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