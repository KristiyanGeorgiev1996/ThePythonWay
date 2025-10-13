penPacketPrice = 5.80
markerPacketPrice = 7.20
cleanerLiterPrice = 1.20

penPacketsCount = int(input())
markerPacketsCount = int(input())
cleanerLitresCount = float(input())
percentDiscount = float(input())

bill = penPacketPrice * penPacketsCount + markerPacketPrice * markerPacketsCount + cleanerLiterPrice * cleanerLitresCount
billWithDiscount = bill - (bill * percentDiscount / 100)

print(billWithDiscount)
