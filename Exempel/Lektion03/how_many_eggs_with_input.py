# Hur många äggkartonger ska vi köpa?
# Notera att vi kan få oönskade resultat då vi enbart har två möjliga
# fall i vår if-sats.

store_sells_loaves_of_bread = input("Säljer butiken limpor? True eller False: ")

if store_sells_loaves_of_bread == "True":
    egg_boxes_to_buy = 2
else:
    egg_boxes_to_buy = 1

print("Det blev", egg_boxes_to_buy, "äggkartonger!")
