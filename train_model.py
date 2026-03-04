import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Données d'exemple
data = pd.DataFrame({
    "Puissance_kVA":[250,400,630,800,1000,1200],
    "Icc_kA":[25,25,36,36,50,50],
    "Temp_C":[35,40,45,45,40,45],
    "DJ_A":[400,630,1000,1000,1600,1600]
})

X = data[["Puissance_kVA","Icc_kA","Temp_C"]]
y = data["DJ_A"]

# Entraînement
model = RandomForestClassifier()
model.fit(X,y)

# Sauvegarde du modèle
joblib.dump(model,"modele.pkl")
print("Modèle IA créé avec succès")