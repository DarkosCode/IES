import torch

SEMILLA = 912
torch.manual_seed(SEMILLA)
if torch.cuda.is_available(): # GPU Nvidia
    torch.cuda.manual_seed_all(SEMILLA)
if torch.backends.mps.is_available(): # Apple
    torch.mps.manual_seed(SEMILLA)

# y = m * x + b
M = 3.0
B = 6.66
x = torch.tensor([[2.0], [4.0], [6.0], [8.0], [10.0], [12.0], [14.0]])
y = M * x + B

w = torch.randn(1, requires_grad=True)
b = torch.randn(1, requires_grad=True)

tasa_de_aprendizaje = 0.001

for epoca in range(15_000):
    y_prediccion = w * x + b
    perdida = torch.mean((y_prediccion - y) ** 2)
    perdida.backward()
    with torch.no_grad():
        w -= tasa_de_aprendizaje * w.grad
        b -= tasa_de_aprendizaje * b.grad
        w.grad.zero_()
        b.grad.zero_()

print(f"Pendiente esperada: {M}. Pendiente obtenida: {w.item():.2f}")
print(f"Ordenada al origen esperada: {B}. Ordenada al origen obtenida: {b.item():.2f}.")

X1 = 16.0
y1 = w * X1 + b
print(f"Esperado: {X1} -> {M * X1 + B}. Obtenido: {X1} -> {y1.item():.2f}")