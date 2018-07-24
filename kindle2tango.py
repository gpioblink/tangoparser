#coding:UTF-8
import sys

from pyquery import PyQuery as pq
import csv

reload(sys)
sys.setdefaultencoding('utf-8')
print 'defaultencoding:', sys.getdefaultencoding()

args = sys.argv

with open(args[1],'r') as info:
    #with open('test.csv','a') as output:
    with open('output.csv','a') as output:
        writer = csv.writer(output, lineterminator='\n', delimiter='\t')
        book = pq(info.read(), parser='html')
        tag = book.find('.k-solid.k-white.bd-corner-10').text() + book.find('.m-bottom-0em75').find('.font-090per.bold').text() + " " + book.find('.font-160per.bold').text()
        print(tag)
        for page in book.find('.k-solid-top.k-2px'):
            section = pq(page)
            entry = section.find('.bg-gainsboro.p-right-0em50.p-bottom-0em50.p-left-0em50')
            if entry.text() == "" :
                continue
            title = entry.find('.font-150per.bold').text()
            wordId = entry.find('.k-solid.font-090per.inverse.p-left-0em25.p-right-0em25').text()
            symbol = entry.find('.phonetic_symbols').outerHtml()
            answer = section.find('.p-0em50').outerHtml()
            if isinstance(answer,type(None)):
                #「でちゃうくん」の後ろのエントリは変則的なので後で処理
                print("Error Dechau\t"+ wordId +"\t"+ title +"\t")
                continue

            print(wordId +"\t"+ title +"\t")
            writer.writerow([title,symbol+"\n"+answer+"\n"+wordId,tag])
            #output.write(answer+"\n")

        for page in book.find('.float-clear'):
            #「でちゃうくん」の後ろの処理
            section =pq(page)
            entry = section.find('.bg-gainsboro.p-right-0em50.p-bottom-0em50.p-left-0em50')
            if entry.text() == "" :
                continue
            title = entry.find('.font-150per.bold').text()
            wordId = entry.find('.k-solid.font-090per.inverse.p-left-0em25.p-right-0em25').text()
            symbol = entry.find('.phonetic_symbols').outerHtml()
            answer = section.find('.p-0em50').outerHtml()

            print(wordId +"\t"+ title +"\t")
            writer.writerow([title,symbol+"\n"+answer+"\n"+wordId,tag])
            #output.write(answer+"\n")
