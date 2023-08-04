from logicversions import logicv1ATRMACD



def logics(symbol): 
    profitv1 = {}
    profitv2_001 = {}
    profitv2_003 = {}
    profitv4 = {}
    profitv5_001 = {} #1_003
    profitv5_003 = {}
    profitv1.clear()
    profitv2_001.clear()
    profitv2_003.clear()
    profitv4.clear()
    profitv5_001.clear()
    profitv5_003.clear()
    try:
        profitv1['Mar2023'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","15m ago")
        '''
        profitv2_001['Feb2023'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","15m ago",df0)
        profitv2_003['Feb2023'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","15m ago",df0)
        profitv4['Feb2023'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","15m ago",df0)
        profitv5_001['Feb2023'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","15m ago",df0)
        profitv5_003['Feb2023'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","15m ago",df0)
        '''
    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003
    
    try:
        profitv1['Feb2023'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","1 Mar 2023")
        '''
        profitv2_001['Feb2023'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","15m ago",df0)
        profitv2_003['Feb2023'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","15m ago",df0)
        profitv4['Feb2023'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","15m ago",df0)
        profitv5_001['Feb2023'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","15m ago",df0)
        profitv5_003['Feb2023'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","15m ago",df0)
        '''
    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003
    try:
        profitv1['Jan2023'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","1 Feb 2023")
        '''
        profitv2_001['Jan2023'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","1 Feb 2023",df1)
        profitv2_003['Jan2023'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","1 Feb 2023",df1)
        '''
        '''
        profitv4['Jan2023'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","1 Feb 2023",df1)
        profitv5_001['Jan2023'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","1 Feb 2023",df1)
        profitv5_003['Jan2023'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","1 Feb 2023",df1)
        '''
    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003
    try:
        profitv1['Dec2022'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","1 Jan 2023")
        '''
        profitv2_001['Dec2022'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","1 Jan 2023",df2)
        profitv2_003['Dec2022'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","1 Jan 2023",df2)
        '''
        '''
        profitv4['Dec2022'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","1 Jan 2023",df2)
        profitv5_001['Dec2022'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","1 Jan 2023",df2)
        profitv5_003['Dec2022'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","1 Jan 2023",df2)
        '''
    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003
    try:
        profitv1['Nov2022'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","1 Dec 2022")
        '''
        profitv2_001['Nov2022'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","1 Dec 2022",df3)
        profitv2_003['Nov2022'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","1 Dec 2022",df3)
        '''
        '''
        profitv4['Nov2022'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","1 Dec 2022",df3)
        profitv5_001['Nov2022'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","1 Dec 2022",df3)
        profitv5_003['Nov2022'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","1 Dec 2022",df3)
        '''
    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003
    try:
        profitv1['Oct2022'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","1 Nov 2022")
        '''
        profitv2_001['Oct2022'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","1 Nov 2022",df4)
        profitv2_003['Oct2022'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","1 Nov 2022",df4)
        '''
        '''
        profitv4['Oct2022'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","1 Nov 2022",df4)
        profitv5_001['Oct2022'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","1 Nov 2022",df4)
        profitv5_003['Oct2022'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","1 Nov 2022",df4)
        '''
    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003
    try:
        profitv1['Sep2022'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","1 Oct 2022")
        '''
        profitv2_001['Sep2022'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","1 Oct 2022",df5)
        profitv2_003['Sep2022'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","1 Oct 2022",df5)
        '''
        '''
        profitv4['Sep2022'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","1 Oct 2022",df5)
        profitv5_001['Sep2022'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","1 Oct 2022",df5)
        profitv5_003['Sep2022'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","1 Oct 2022",df5)
        '''

    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003
    try:
        profitv1['Aug2022'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","1 Sep 2022")
        '''
        profitv2_001['Aug2022'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","1 Sep 2022",df6)
        profitv2_003['Aug2022'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","1 Sep 2022",df6)
        '''
        '''
        profitv4['Aug2022'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","1 Sep 2022",df6)
        profitv5_001['Aug2022'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","1 Sep 2022",df6)
        profitv5_003['Aug2022'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","1 Sep 2022",df6)
        '''

    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003
    try:
        profitv1['Jul2022'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","1 Aug 2022")
        '''
        profitv2_001['Jul2022'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","1 Aug 2022",df7)
        profitv2_003['Jul2022'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","1 Aug 2022",df7)
        '''
        '''
        profitv4['Jul2022'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","1 Aug 2022",df7)
        profitv5_001['Jul2022'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","1 Aug 2022",df7)
        profitv5_003['Jul2022'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","1 Aug 2022",df7)
        '''
        
    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003
    try: 
        profitv1['Jun2022'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","1 Jul 2022")
        '''
        profitv2_001['Jun2022'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","1 Jul 2022",df8)
        profitv2_003['Jun2022'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","1 Jul 2022",df8)
        '''
        '''
        profitv4['Jun2022'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","1 Jul 2022",df8)
        profitv5_001['Jun2022'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","1 Jul 2022",df8)
        profitv5_003['Jun2022'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","1 Jul 2022",df8)
        '''
    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003
    try: 
        profitv1['May2022'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","1 Jun 2022")
        '''
        profitv2_001['May2022'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","1 Jun 2022",df9)
        profitv2_003['May2022'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","1 Jun 2022",df9)
        '''
        '''
        profitv4['May2022'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","1 Jun 2022",df9)
        profitv5_001['May2022'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","1 Jun 2022",df9)
        profitv5_003['May2022'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","1 Jun 2022",df9)
        '''
    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003        
    try: 
        profitv1['Apr2022'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","1 May 2022")
        '''
        profitv2_001['Apr2022'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","1 May 2022",df10)
        profitv2_003['Apr2022'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","1 May 2022",df10)
        '''
        '''
        profitv4['Apr2022'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","1 May 2022",df10)
        profitv5_001['Apr2022'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","1 May 2022",df10)
        profitv5_003['Apr2022'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","1 May 2022",df10)
        '''
    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003
    try: 
        profitv1['Mar2022'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","1 Apr 2022")
        '''
        profitv2_001['Mar2022'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","1 Apr 2022",df11)
        profitv2_003['Mar2022'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","1 Apr 2022",df11)
        '''
        '''
        profitv4['Mar2022'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","1 Apr 2022",df11)
        profitv5_001['Mar2022'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","1 Apr 2022",df11)
        profitv5_003['Mar2022'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","1 Apr 2022",df11)
        '''
    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003
    try: 
        profitv1['Feb2022'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","1 Mar 2022")
        '''
        profitv2_001['Feb2022'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","1 Mar 2022",df12)
        profitv2_003['Feb2022'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","1 Mar 2022",df12)
        '''
        '''
        profitv4['Feb2022'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","1 Mar 2022",df12)
        profitv5_001['Feb2022'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","1 Mar 2022",df12)
        profitv5_003['Feb2022'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","1 Mar 2022",df12)
        '''

    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003  
    try:      
        profitv1['Jan2022'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","1 Feb 2022")
        '''
        profitv2_001['Jan2022'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","1 Feb 2022",df13)
        profitv2_003['Jan2022'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","1 Feb 2022",df13)
        '''
        '''
        profitv4['Jan2022'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","1 Feb 2022",df13)
        profitv5_001['Jan2022'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","1 Feb 2022",df13)
        profitv5_003['Jan2022'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","1 Feb 2022",df13)
        '''
    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003
    try: 
        profitv1['Dec2021'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","1 Jan 2022")
        '''
        profitv2_001['Dec2021'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","1 Jan 2022",df14)
        profitv2_003['Dec2021'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","1 Jan 2022",df14)
        '''
        '''
        profitv4['Dec2021'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","1 Jan 2022",df14)
        profitv5_001['Dec2021'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","1 Jan 2022",df14)
        profitv5_003['Dec2021'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","1 Jan 2022",df14)
        '''
    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003
    try: 
        profitv1['Nov2021'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","1 Dec 2021")
        '''
        profitv2_001['Nov2021'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","1 Dec 2021",df15)
        profitv2_003['Nov2021'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","1 Dec 2021",df15)
        '''
        '''
        profitv4['Nov2021'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","1 Dec 2021",df15)
        profitv5_001['Nov2021'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","1 Dec 2021",df15)
        profitv5_003['Nov2021'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","1 Dec 2021",df15)
        '''
    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003
    try: 
        profitv1['Oct2021'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","1 Nov 2021")
        '''
        profitv2_001['Oct2021'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","1 Nov 2021",df16)
        profitv2_003['Oct2021'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","1 Nov 2021",df16)
        '''
        '''
        profitv4['Oct2021'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","1 Nov 2021",df16)
        profitv5_001['Oct2021'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","1 Nov 2021",df16)
        profitv5_003['Oct2021'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","1 Nov 2021",df16)
        '''
    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003
    try: 
        profitv1['Sep2021'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","1 Oct 2021")
        '''
        profitv2_001['Sep2021'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","1 Oct 2021",df17)
        profitv2_003['Sep2021'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","1 Oct 2021",df17)
        '''
        '''
        profitv4['Sep2021'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","1 Oct 2021",df17)
        profitv5_001['Sep2021'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","1 Oct 2021",df17)
        profitv5_003['Sep2021'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","1 Oct 2021",df17)
        '''
    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003
    try: 
        profitv1['Aug2021'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","1 Sep 2021")
        '''
        profitv2_001['Aug2021'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","1 Sep 2021",df18)
        profitv2_003['Aug2021'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","1 Sep 2021",df18)
        '''
        '''
        profitv4['Aug2021'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","1 Sep 2021",df18)
        profitv5_001['Aug2021'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","1 Sep 2021",df18)
        profitv5_003['Aug2021'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","1 Sep 2021",df18)
        '''
    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003
    try: 
        profitv1['Jul2021'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","1 Aug 2021")
        '''
        profitv2_001['Jul2021'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","1 Aug 2021",df19)
        profitv2_003['Jul2021'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","1 Aug 2021",df19)
        '''
        '''
        profitv4['Jul2021'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","1 Aug 2021",df19)
        profitv5_001['Jul2021'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","1 Aug 2021",df19)
        profitv5_003['Jul2021'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","1 Aug 2021",df19)
        '''
    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003 
    try: 
        profitv1['Jun2021'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","1 Jul 2021")
        '''
        profitv2_001['Jun2021'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","1 Jul 2021",df20)
        profitv2_003['Jun2021'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","1 Jul 2021",df20)
        '''
        '''
        profitv4['Jun2021'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","1 Jul 2021",df20)
        profitv5_001['Jun2021'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","1 Jul 2021",df20)
        profitv5_003['Jun2021'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","1 Jul 2021",df20)
        '''
    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003
    try: 
        profitv1['May2021'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","1 Jun 2021")
        '''
        profitv2_001['May2021'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","1 Jun 2021",df21)
        profitv2_003['May2021'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","1 Jun 2021",df21)
        '''
        '''
        profitv4['May2021'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","1 Jun 2021",df21)
        profitv5_001['May2021'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","1 Jun 2021",df21)
        profitv5_003['May2021'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","1 Jun 2021",df21)
        '''
    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003
    try: 
        profitv1['Apr2021'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","1 May 2021")
        '''
        profitv2_001['Apr2021'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","1 May 2021",df22)
        profitv2_003['Apr2021'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","1 May 2021",df22)
        '''
        '''
        profitv4['Apr2021'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","1 May 2021",df22)
        profitv5_001['Apr2021'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","1 May 2021",df22)
        profitv5_003['Apr2021'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","1 May 2021",df22)
        '''
    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003
    try: 
        profitv1['Mar2021'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","1 Apr 2021")
        '''
        profitv2_001['Mar2021'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","1 Apr 2021",df23)
        profitv2_003['Mar2021'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","1 Apr 2021",df23)
        '''
        '''
        profitv4['Mar2021'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","1 Apr 2021",df23)
        profitv5_001['Mar2021'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","1 Apr 2021",df23)
        profitv5_003['Mar2021'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","1 Apr 2021",df23)
        '''
    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003
    try: 
        profitv1['Feb2021'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","1 Mar 2021")
        '''
        profitv2_001['Feb2021'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","1 Mar 2021",df24)
        profitv2_003['Feb2021'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","1 Mar 2021",df24)
        '''
        '''
        profitv4['Feb2021'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","1 Mar 2021",df24)
        profitv5_001['Feb2021'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","1 Mar 2021",df24)
        profitv5_003['Feb2021'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","1 Mar 2021",df24)
        '''
    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003
    try: 
        profitv1['Jan2021'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","1 Feb 2021")
        '''
        profitv2_001['Jan2021'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","1 Feb 2021",df25)
        profitv2_003['Jan2021'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","1 Feb 2021",df25)
        '''
        '''
        profitv4['Jan2021'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","1 Feb 2021",df25)
        profitv5_001['Jan2021'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","1 Feb 2021",df25)
        profitv5_003['Jan2021'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","1 Feb 2021",df25)
        '''
    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003
    try: 
        profitv1['Dec2020'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","1 Jan 2021")
        '''
        profitv2_001['Dec2020'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","1 Jan 2021",df26)
        profitv2_003['Dec2020'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","1 Jan 2021",df26)
        '''
        '''
        profitv4['Dec2020'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","1 Jan 2021",df26)
        profitv5_001['Dec2020'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","1 Jan 2021",df26)
        profitv5_003['Dec2020'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","1 Jan 2021",df26)
        '''
    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003
    try: 
        profitv1['Nov2020'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","1 Dec 2020")
        '''
        profitv2_001['Nov2020'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","1 Dec 2020",df27)
        profitv2_003['Nov2020'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","1 Dec 2020",df27)
        '''
        '''
        profitv4['Nov2020'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","1 Dec 2020",df27)
        profitv5_001['Nov2020'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","1 Dec 2020",df27)
        profitv5_003['Nov2020'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","1 Dec 2020",df27)
        '''
    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003
    try:  
        profitv1['Oct2020'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","1 Nov 2020")
        '''
        profitv2_001['Oct2020'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","1 Nov 2020",df28)
        profitv2_003['Oct2020'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","1 Nov 2020",df28)
        '''
        '''
        profitv4['Oct2020'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","1 Nov 2020",df28)
        profitv5_001['Oct2020'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","1 Nov 2020",df28)
        profitv5_003['Oct2020'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","1 Nov 2020",df28)
        '''
    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003
    try: 
        profitv1['Sep2020'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","1 Oct 2020")
        '''
        profitv2_001['Sep2020'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","1 Oct 2020",df29)
        profitv2_003['Sep2020'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","1 Oct 2020",df29)
        '''
        '''
        profitv4['Sep2020'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","1 Oct 2020",df29)
        profitv5_001['Sep2020'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","1 Oct 2020",df29)
        profitv5_003['Sep2020'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","1 Oct 2020",df29)
        '''
    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003
    try: 
        profitv1['Aug2020'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","1 Sep 2020")
        '''
        profitv2_001['Aug2020'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","1 Sep 2020",df30)
        profitv2_003['Aug2020'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","1 Sep 2020",df30)
        '''
        '''
        profitv4['Aug2020'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","1 Sep 2020",df30)
        profitv5_001['Aug2020'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","1 Sep 2020",df30)
        profitv5_003['Aug2020'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","1 Sep 2020",df30)
        '''
    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003
    try: 
        profitv1['Jul2020'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","1 Aug 2020")
        '''
        profitv2_001['Jul2020'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","1 Aug 2020",df31)
        profitv2_003['Jul2020'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","1 Aug 2020",df31)
        '''
        '''
        profitv4['Jul2020'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","1 Aug 2020",df31)
        profitv5_001['Jul2020'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","1 Aug 2020",df31)
        profitv5_003['Jul2020'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","1 Aug 2020",df31)
        '''
    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003
    try: 
        profitv1['Jun2020'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","1 Jul 2020")
        '''
        profitv2_001['Jun2020'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","1 Jul 2020",df32)
        profitv2_003['Jun2020'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","1 Jul 2020",df32)
        '''
        '''
        profitv4['Jun2020'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","1 Jul 2020",df32)
        profitv5_001['Jun2020'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","1 Jul 2020",df32)
        profitv5_003['Jun2020'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","1 Jul 2020",df32)
        '''
    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003 
    try: 
        profitv1['May2020'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","1 Jun 2020")
        '''
        profitv2_001['May2020'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","1 Jun 2020",df33)
        profitv2_003['May2020'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","1 Jun 2020",df33)
        '''
        '''
        profitv4['May2020'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","1 Jun 2020",df33)
        profitv5_001['May2020'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","1 Jun 2020",df33)
        profitv5_003['May2020'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","1 Jun 2020",df33)
        '''
    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003
    try: 
        profitv1['Apr2020'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","1 May 2020")
        '''
        profitv2_001['Apr2020'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","1 May 2020",df34)
        profitv2_003['Apr2020'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","1 May 2020",df34)
        '''
        '''
        profitv4['Apr2020'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","1 May 2020",df34)
        profitv5_001['Apr2020'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","1 May 2020",df34)
        profitv5_003['Apr2020'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","1 May 2020",df34)
        '''
    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003
    try: 
        profitv1['Mar2020'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","1 Apr 2020")
        '''
        profitv2_001['Mar2020'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","1 Apr 2020",df35)
        profitv2_003['Mar2020'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","1 Apr 2020",df35)
        '''
        '''
        profitv4['Mar2020'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","1 Apr 2020",df35)
        profitv5_001['Mar2020'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","1 Apr 2020",df35)
        profitv5_003['Mar2020'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","1 Apr 2020",df35)
        '''
    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003
    try: 
        profitv1['Feb2020'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","1 Mar 2020")
        '''
        profitv2_001['Feb2020'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","1 Mar 2020",df36)
        profitv2_003['Feb2020'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","1 Mar 2020",df36)
        '''
        '''
        profitv4['Feb2020'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","1 Mar 2020",df36)
        profitv5_001['Feb2020'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","1 Mar 2020",df36)
        profitv5_003['Feb2020'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","1 Mar 2020",df36)
        '''
    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003 
    try: 
        profitv1['Jan2020'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","1 Feb 2020")
        '''
        profitv2_001['Jan2020'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","1 Feb 2020",df37)
        profitv2_003['Jan2020'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","1 Feb 2020",df37)
        '''
        '''
        profitv4['Jan2020'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","1 Feb 2020",df37)
        profitv5_001['Jan2020'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","1 Feb 2020",df37)
        profitv5_003['Jan2020'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","1 Feb 2020",df37)
        '''
    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003
    try: 
        profitv1['Dec2019'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","1 Jan 2020")
        '''
        profitv2_001['Dec2019'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","1 Jan 2020",df38)
        profitv2_003['Dec2019'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","1 Jan 2020",df38)
        '''
        '''
        profitv4['Dec2019'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","1 Jan 2020",df38)
        profitv5_001['Dec2019'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","1 Jan 2020",df38)
        profitv5_003['Dec2019'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","1 Jan 2020",df38)
        '''
    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003
    try: 
        profitv1['Nov2019'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","1 Dec 2019")
        '''
        profitv2_001['Nov2019'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","1 Dec 2019",df39)
        profitv2_003['Nov2019'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","1 Dec 2019",df39)
        '''
        '''
        profitv4['Nov2019'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","1 Dec 2019",df39)
        profitv5_001['Nov2019'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","1 Dec 2019",df39)
        profitv5_003['Nov2019'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","1 Dec 2019",df39)
        '''
    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003
    try:  
        profitv1['Oct2019'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","1 Nov 2019")
        '''
        profitv2_001['Oct2019'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","1 Nov 2019",df40)
        profitv2_003['Oct2019'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","1 Nov 2019",df40)
        '''
        '''
        profitv4['Oct2019'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","1 Nov 2019",df40)
        profitv5_001['Oct2019'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","1 Nov 2019",df40)
        profitv5_003['Oct2019'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","1 Nov 2019",df40)
        '''
    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003
    try: 
        profitv1['Sep2019'] = logicv1ATRMACD.history(symbol,"1 Jan 2020","1 Oct 2019")
        '''
        profitv2_001['Sep2019'] = logicv1ATRMACDv2_1_001.history(symbol,"1 Jan 2020","1 Oct 2019",df41)
        profitv2_003['Sep2019'] = logicv1ATRMACDv2_1_003.history(symbol,"1 Jan 2020","1 Oct 2019",df41)
        '''
        '''
        profitv4['Sep2019'] = logicv1ATRMACDv4.history(symbol,"1 Jan 2020","1 Oct 2019",df41)
        profitv5_001['Sep2019'] = logicv1ATRMACDv5_1_001.history(symbol,"1 Jan 2020","1 Oct 2019",df41)
        profitv5_003['Sep2019'] = logicv1ATRMACDv5_1_003.history(symbol,"1 Jan 2020","1 Oct 2019",df41)
        '''
    except:
        print("err")
        return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003

    return profitv1#,profitv2_001,profitv2_003#,profitv4,profitv5_001,profitv5_003
    