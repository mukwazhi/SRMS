import sqlite3


class DAO:
    @staticmethod
    def add_transction(**transaction):
        try:
            db_file = "C:\\Users\\bmukwazhi.NHSZIM\\PycharmProjects\\CargoProject\\cargoenv\\cargopro\\cargo_db.sqlite3"
            conn = sqlite3.connect(db_file)
            print("opened connection successfully!")
            cur = conn.cursor()
            # cur.execute("select * from compute_transcations")
            cur.execute("INSERT INTO  compute_transcations (station,flightNumber, flightDate, routing,arrivalTime,"
                        "departureTime,cargoIn, cargoOut, mailIn, mailOut, paxIn, paxOut, pad, asu, gpu) "
                        "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                        (transaction['flight'],
                         transaction['invoice'],
                         transaction['awb'],
                         transaction['hwb'],
                         transaction['arrival_date'],
                         transaction['dispatch'],
                         transaction['weight'],
                         transaction["units"],
                         transaction['special'],
                         transaction['perishable'],
                         transaction['delay'],
                         transaction['storage'],
                         transaction['break_bulk'],
                         transaction['agency'],
                         transaction['charge'],
                         transaction['coldroom_charge'],
                         transaction['delay'],
                         transaction['vat'],
                         transaction['total'],
                         transaction['tender'],
                         transaction['station'],
                         ))
            conn.commit()
            print("database written")
            rows = cur.fetchall()
            print(rows)
            for row in rows:
                print(row)
            conn.close()
        except sqlite3.Error as e:
            print("failed")
            print(e)

        return None
