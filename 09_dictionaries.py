#word= key(dit is de unieke identifier in de dicttionairy) en value is de echte definitei

#wij gaan een programma maken die een maand van 2 letters omzet naar de volle maand naam
#dus jan => Januery | feb omzet naar FEbruaie
#dicttionairy wordt altijd gemaak  met open en closing{}

maand_conversie = {
    "Jan" : "Januari",
    "Feb" : "Februari",
    "May" : "May",
    "Jun" : "Juni",
    "Jul" : "Juli",
    "Aug" : "Augustus",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "Decemeber",
}
#nu hebben key value pairs

print(maand_conversie["Nov"])
#ik kan referen aan de key en het geeft me de volledige naam
#print(maand_conversie["liefde"])
print(maand_conversie.get("Liefde", "geen valide sleutel"))
#keys kunnen ook nummers zijn, zolang ze uniek zien
