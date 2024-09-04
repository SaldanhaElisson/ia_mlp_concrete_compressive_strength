import sys


sys.path.append('/home/marvin/PycharmProjects/IA_CCS/data_handling')

import torch
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from torch import optim
import torch.nn.functional as F

from data_handling.cleassing_datas import CleasingDatas
from data_handling.data_main import DataMain
from models_ia.mlp.model import MLP


def plot_scatter(predictions, y_test):
    plt.scatter(y_test, predictions, label='Predições')
    plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', label='Ideal')
    plt.xlabel('Saída Desejada')
    plt.ylabel('Predição')
    plt.legend()
    plt.show()


class HandlerTrainer():

    def __init__(self,  n_layers, n_hidden, lr, epochs, num_repeat):
        self.num_repeat = num_repeat
        self.lr = lr
        self.x_test = None
        self.y_test = None
        self.y_val = None
        self.x_val = None
        self.y_train = None
        self.x_train = None
        self.n_inputs = 8
        self.n_outputs = 1
        self.n_layers = n_layers
        self.n_hidden = n_hidden
        self.epochs = epochs
        self.model = MLP(self.n_inputs, self.n_outputs, n_layers, n_hidden)


    def set_datas(self):
        # Carregar e limpar os dados
        path_file = "../../concrete_data.xls"
        data_main = DataMain(path_file=path_file)
        data_cleaned, num_outliers = CleasingDatas.remove_outliers(data_main.data_set)
        data_main_cleaned = DataMain(data_frame=data_cleaned)
        data_frame = data_main_cleaned.data_set

        # print(f"Número de outliers removidos: {num_outliers}")

        x = torch.tensor(data_frame.iloc[:, :-1].values, dtype=torch.float32)
        y = torch.tensor(data_frame.iloc[:, -1].values, dtype=torch.float32)

        # Normalizar as features
        scaler = MinMaxScaler()
        x_normalized = scaler.fit_transform(x)

        scaler_y = MinMaxScaler()
        y_normalized = scaler_y.fit_transform(y.reshape(-1, 1)).flatten()

        # Converter para tensores
        x_normalized = torch.tensor(x_normalized, dtype=torch.float32)
        y_normalized = torch.tensor(y_normalized, dtype=torch.float32)

        # Primeira divisão: 60% para treinamento, 40% para teste e validação
        x_train, x_temp, y_train, y_temp = train_test_split(x_normalized, y_normalized, test_size=0.4, random_state=42)

        # Segunda divisão: 75% dos 40% para teste (30% do total), 25% dos 40% para validação (10% do total)
        x_test, x_val, y_test, y_val = train_test_split(x_temp, y_temp, test_size=0.25, random_state=42)

        # Converter para tensores
        self.x_train = torch.tensor(x_train, dtype=torch.float32)
        self.y_train = torch.tensor(y_train, dtype=torch.float32)
        self.x_val = torch.tensor(x_val, dtype=torch.float32)
        self.y_val = torch.tensor(y_val, dtype=torch.float32)
        self.x_test = torch.tensor(x_test, dtype=torch.float32)
        self.y_test = torch.tensor(y_test, dtype=torch.float32)

    def train(self):

            self.model.train()
            optimizer = optim.Adam(self.model.parameters(), lr=self.lr)

            losses = []
            val_losses = []
            test_losses = []
            num_epochs = self.epochs
            for epoch in range(num_epochs):  # número de épocas
                # Embaralhar os dados
                permutation = torch.randperm(self.x_train.size()[0])
                epoch_loss = 0.0
                for n in permutation:
                    optimizer.zero_grad()

                    y_hat = self.model(self.x_train[n])
                    loss = F.mse_loss(y_hat, self.y_train[n])  # Função de perda
                    loss.backward()

                    torch.nn.utils.clip_grad_norm_(self.model.parameters(), max_norm=1.0)
                    optimizer.step()
                    epoch_loss += loss.item()

                epoch_loss /= self.x_train.size()[0]
                losses.append(epoch_loss)

                # Avaliar no conjunto de teste
                self.model.eval()

                test_loss = 0.0
                with torch.no_grad():
                    for n in range(self.x_test.size()[0]):
                        y_hat = self.model(self.x_test[n])
                        test_loss += F.mse_loss(y_hat, self.y_test[n]).item()
                test_loss /= self.x_test.size()[0]
                test_losses.append(test_loss)

                self.model.train()

                if (epoch + 1) % 1 == 0:
                    print(
                        f'Epoch [{epoch + 1}/{num_epochs}], Loss: {epoch_loss:.4f}, Test Loss: {test_loss:.4f}')

            print(f"Resultados do Treinamento { self.num_repeat }/5")
            print("Training Losses:", losses)
            print("Validation Losses:", val_losses)
            print("Test Losses:", test_losses)

            # Plotar o gráfico de aprendizagem
            plt.plot(range(num_epochs), losses, label='Training Loss')
            plt.plot(range(num_epochs), test_losses, label='Test Loss')
            plt.xlabel('Epoch')
            plt.ylabel('Loss')
            plt.title(f'Learning Curve - Treinamento - {self.num_repeat} - Nós e Camadas - {self.n_hidden} - {self.n_layers}')
            plt.legend()
            plt.show()

    def evaluate_model(self):
        self.model.eval()
        test_loss_mse = 0.0
        test_loss_mae = 0.0
        predictions = []
        with torch.no_grad():
            for n in range(self.x_test.size()[0]):
                y_hat = self.model(self.x_test[n])
                y_hat = y_hat.squeeze()
                predictions.append(y_hat.item())
                test_loss_mse += F.mse_loss(y_hat, self.y_test[n], reduction='sum').item()
                test_loss_mae += F.l1_loss(y_hat, self.y_test[n], reduction='sum').item()

        test_loss_mse /= self.x_test.size()[0]
        test_loss_mae /= self.x_test.size()[0]
        return {'mse': test_loss_mse, 'mae': test_loss_mae, 'predictions': predictions}
