from sources.cnbcindonesia import CNBCIndonesia
from sources.detikfinance import DetikFinance
from sources.emitennews import EmitenNews
from sources.idxchannel import IDXChannel
from sources.kontan import Kontan


def main():
    cnbcindonesia = CNBCIndonesia()
    detikfinance = DetikFinance()
    emitennews = EmitenNews()
    idxchannel = IDXChannel()
    kontan = Kontan()
   
    keyword = input("Enter a keyword: ")
    
    cnbc_results = cnbcindonesia.keyword_cnbcindonesia([keyword.capitalize()])  
    detikfinance_results = detikfinance.keyword_detikfinance([keyword.capitalize()])
    emitennews_results = emitennews.keyword_emitennews([keyword.capitalize()])
    idx_results = idxchannel.keyword_idxchannel([keyword.capitalize()])  
    kontan_results = kontan.keyword_kontan([keyword.capitalize()])


    ##cnbc output
    print("=" * 50)
    print("CNBC INDONESIA RESULTS")
    print("=" * 50)
    if cnbc_results:
        for result in cnbc_results:
            print(f"Keyword: {result['keyword']}")
            print(f"{result['date']} | {result['title']}")
            print(result['link'])
            print()
    else:
        print("No results found from CNBC Indonesia")
        print()

    ##detikfinance output
    print("=" * 50)
    print("DETIK FINANCE RESULTS")
    print("=" * 50)
    if detikfinance_results:
        for result in detikfinance_results:
            print(f"Keyword: {result['keyword']}")
            print(f"{result['date']} | {result['title']}")
            print(result['link'])
            print()
    else:
        print("No results found from Detik Finance")
        print()

    ##emitennews output
    print("=" * 50)
    print("EMITEN NEWS RESULTS")
    print("=" * 50)
    if emitennews_results:
        for result in emitennews_results:
            print(f"Keyword: {result['keyword']}")
            print(f"{result['date']} | {result['title']}")
            print(result['link'])
            print()
    else:
        print("No results found from Emiten News")
        print()
    
    ##idxchannel output
    print("=" * 50)
    print("IDX CHANNEL RESULTS")
    print("=" * 50)
    if idx_results:
        for result in idx_results:
            print(f"Keyword: {result['keyword']}")
            print(f"{result['date']} | {result['title']}")
            print(result['link'])
            print()
    else:
        print("No results found from IDX Channel")
        print()

    ##kontan output
    print("=" * 50)
    print("KONTAN RESULTS")
    print("=" * 50)
    if kontan_results:
        for result in kontan_results:
            print(f"Keyword: {result['keyword']}")
            print(f"{result['date']} | {result['title']}")
            print(result['link'])
            print()
    else:
        print("No results found from Kontan")
        print()



if __name__ == "__main__":
    main()