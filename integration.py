import pandas as pd
import pickle


with open('hist.pkl', 'rb') as f:
    hist = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('modele.pkl', 'rb') as f:
    model = pickle.load(f)



def preprocessing(x):
    categorical = x
    categorical_columns = categorical.columns
    num=0
    for col in (categorical_columns):
        le = hist[num]
        x[col] = le.transform(x[col])
        num+=1
    x = scaler.transform(x)
    return x


def Cleaning(df):   
    df["Mobilité"] = df["Mobilité"].astype(str)
    df = df.applymap(lambda x: x.strip().lower() if isinstance(x, str) else x)
    x = df
    x['Douleur Spontanée'] = x['Douleur Spontanée'].replace({'oui irradiante vers l\'oreil': 'irradiante',
                                                             'occassionnellement': 'occasionnelle'})

    # Douleur Provoquée
    x['Douleur Provoquée'] = x['Douleur Provoquée'].replace('parfois a la mastication','au contact')
    x['Douleur Provoquée'] = x['Douleur Provoquée'].replace( 'mastication','au contact')

    # Col "" Mobilité ""
    x['Mobilité'] = x['Mobilité'].replace('1', 'one')
    x['Mobilité'] = x['Mobilité'].replace('1+', 'one_plus')

    # Col "" Vitalité ""
    x['Vitalité'] = x['Vitalité'].replace('vivante', 'dent vivante')
    x['Vitalité'] = x['Vitalité'].replace('oui', 'dent vivante')

    # Col "" Palpation Apicale ""
    x['Palpation Apicale'] = x['Palpation Apicale'].replace('négatif','non')
    x['Palpation Apicale'] = x['Palpation Apicale'].replace('negatif','non')


    # Col "" 'Médication ATG ""
    x['Médication ATG'] = x['Médication ATG'].replace('non', 'non efficace')
    x['Médication ATG'] = x['Médication ATG'].replace('oui', 'efficace')

    # Douleur Spontanée
    x['Soulager '] = x['Soulager '].replace('eviter la mastication','sans contact')
    x['Soulager '] = x['Soulager '].replace('parfois par le froid','froid')

    # Col "" 'Odeur Fétide ""
    x['Médication ATG'] = x['Médication ATG'].replace('odeur fétide', 'oui')

    return x



def pred(data_test):
    x_  = Cleaning(data_test)
    x_ = preprocessing(x_)
    
    return model(x_)
