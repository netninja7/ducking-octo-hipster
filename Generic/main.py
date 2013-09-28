import GA_main as ga

# init for ga(iPopSize,iLenGene,bBinary,fPc,fPm,iGen,iShowGen)
ga = ga.ga(15,26,False,0.9,0.2,5000,5,"crypto_fitness")

ga.create()

ga.run()
