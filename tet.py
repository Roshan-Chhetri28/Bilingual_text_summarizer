import torch

def verificar_torch():
    try:
        print("Torch importado exitosamente")
    # Crear un tensor simple para verificar funcionalidad básica
        tensor = torch.tensor([1.0, 2.0, 3.0])
        print(f"Tensor creado: {tensor}")
        return True
    except Exception as e:
        print(f"Error al importar torch o al crear un tensor: {e}")
        return False

def main():
    verificar_torch()
if __name__ =="__main__":
    main()
    