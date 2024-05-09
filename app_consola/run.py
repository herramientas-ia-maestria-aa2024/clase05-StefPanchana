# ejemplificación
#

# importamos los modelos y el métdodo que predice 
from metodos import load_models, predict

vectoriser, LRmodel = load_models()
mensaje = "fear"
print("%s - %s" % (mensaje, 
            predict(vectoriser, LRmodel, mensaje)
            ))
