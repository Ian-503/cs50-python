meses={
    "January":1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
}
while True:
    try:
        data=input("Date: ").strip()
        if "/" in data:
            mes,dia,ano=data.split("/")
            mes=int(mes)
            dia=int(dia)
            ano=int(ano)

            if 1 <= mes <= 12 and 1 <= dia <= 31:
                print(f"{ano}-{mes:02}-{dia:02}")
                break
            else:
                continue

        elif "," in data:
            mes,dia,ano=data.split(" ")
            mes=mes.title()
            dia=dia.replace(",","")
            if mes in meses:
                mes=meses[mes]
                dia=int(dia)
                if 1 <= dia <= 31:
                    print(f"{ano}-{mes:02}-{dia:02}")
                    break
            else:
                continue
        else:
            continue

    except (ValueError,IndexError):
        pass
