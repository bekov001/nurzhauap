import xlsxwriter


try:
            if any(not el for key, el in self.statics.items()):
                print("\033[33mСтатиски пока нет")
            else:
                workbook = xlsxwriter.Workbook('docs/test.xlsx')
                for key, (item, count) in enumerate(self.statics.items()):
                    name = dec[item].replace(" ", "_")
                    worksheet = workbook.add_worksheet(name)
                    if isinstance(count, list):
                        count = func1(count)
                        for index, (amount, el) in enumerate(count):
                            worksheet.write(index, 0, el)
                            worksheet.write(index, 1, int(amount))
                            chart = workbook.add_chart({'type': 'pie'})

                        # Строим по нашим данным
                        chart.add_series({'values': f'={name}!B1:B{index + 1}',
                                          'categories': f"={name}!A1:A{index + 1}"})

                        worksheet.insert_chart('C3', chart)
                    else:
                        worksheet.write(0, 0, dec[item])
                        worksheet.write(0, 1, count)

                # # Тип диаграммЫ

                workbook.close()
        except Exception:
            print("файл пустой")