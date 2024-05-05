from ucimlrepo import fetch_ucirepo
import pandas as pd

def main():
    try:
        # Define el término de búsqueda
        search_term = "drug"
        print(f"Intentando descargar el conjunto de datos: {search_term}")
        dataset = fetch_ucirepo(name=search_term)
        
        # Verifica si la descarga fue exitosa y si los datos están completos
        if dataset and hasattr(dataset, 'data') and hasattr(dataset.data, 'features') and hasattr(dataset.data, 'targets'):
            X = dataset.data.features
            y = dataset.data.targets
            
            # Especifica la ruta de guardado incluyendo el término de búsqueda en el nombre del archivo
            path_features = f'C:\\Users\\ur\\Desktop\\TFG AFILIAOS\\datasets\\{search_term}_features.csv'
            path_targets = f'C:\\Users\\ur\\Desktop\\TFG AFILIAOS\\datasets\\{search_term}_targets.csv'
            
            # Guarda los datos en archivos CSV
            X.to_csv(path_features, index=False)
            y.to_csv(path_targets, index=False)
            
            print(f"Conjunto de datos descargado y guardado en: '{path_features}' y '{path_targets}'")
        else:
            print("No se pudo descargar el conjunto de datos o los datos descargados están incompletos.")
    except Exception as e:
        print(f"Se produjo un error al intentar descargar los datos: {e}")

if __name__ == "__main__":
    main()
