"""
Taken from
http://pages.physics.cornell.edu/~myers/teaching/ComputationalMethods/ComputerExercises/PythonSoftware/Ising.py

and slightly modified by
Francesc Font-Clos
May 2018
"""
import scipy


class IsingModel:
    """Ising model class."""

    def __init__(self, N=10, T=2. / scipy.log(1. + scipy.sqrt(2.)),
                 H=0., seed=1):
        """
        Call scipy.random.seed with argument seed;
        Set self.N to be N
        Build self.lattice to be random 50/50 0/1, using random_integers
        Call self.SetTemperatureField with T, H
        """
        if seed is None:
            scipy.random.seed()
        else:
            scipy.random.seed(seed)
        self.lattice = scipy.random.random_integers(0, 1, (N, N))
        self.SetTemperatureField(T, H)
        self.N = N

    def SetTemperatureField(self, T, H):
        """
        Sets self.privateTemperature, self.privateField.

        After debugging, for faster performance, set up algorithm-dependent
        data structures to avoid taking exponentials for every flipped spin

        Heat bath algorithm:
        Sets up self.heatBathProbUp to be array of doubles
        of length Z+1=5 (the number of different neighbors up (nUp) possible)
        Figure out spin energies eUp, eDown given nUp; figure out Boltzmann
        relative probabilities boltzUp, boltzDown;
        If T!= 0, set heatBathProbUp(nUp) to boltzUp/(boltzUp+boltzDown)
        otherwise set it to (0, 0.5, 1) if eUp is (positive, zero, negative).
        #
        Metropolis algorithm:
        Sets up self.MetropolisProbUp to be a 2x5 matrix of Floats
        (first index is current state of spin, second index is nUp)
        Iterate over nUp;
          If T != 0
           If eDown > eUp, set probability to flip from down to up to one,
              up to down to 1-exp(-(eDown-eUp)/T)
           If eDown <= eUp, set probability to flip from up to down to one,
              down to up to 1-exp(-(eUp-eDown)/T)
          Otherwise (T=0) set appropriately
        #
        Wolff algorithm
        set p
        """
        self.privateTemperature = T
        self.privateField = H
        J = 1.      # Convention: also float to avoid int problems
        # Set up heat bath algorithm lookup table
        self.heatBathProbUp = scipy.zeros(5, float)
        for nUp in range(0, 5):  # Four neighbors on square lattice
            sumNbrs = 2 * (nUp - 2)  # Sum of spins of neighbors
            eUp = -J * sumNbrs - H
            eDown = J * sumNbrs + H
            if T != 0:
                boltzUp = scipy.exp(-eUp / T)
                boltzDown = scipy.exp(-eDown / T)
                self.heatBathProbUp[nUp] = boltzUp / (boltzUp + boltzDown)
            else:
                if eUp > 0:
                    self.heatBathProbUp[nUp] = 0.
                elif eUp < 0:
                    self.heatBathProbUp[nUp] = 1.
                else:
                    self.heatBathProbUp[nUp] = 0.5
        # Set up Metropolis algorithm lookup table
        self.MetropolisProbUp = scipy.zeros((2, 5), float)
        for nUp in range(0, 5):  # Four neighbors on square lattice
            sumNbrs = 2 * (nUp - 2)  # Sum of spins of neighbors
            eUp = -J * sumNbrs - H
            eDown = J * sumNbrs + H
            if T != 0:
                if eDown > eUp:  # Down spin unstable
                    # If current spin is down, flip up
                    self.MetropolisProbUp[0, nUp] = 1.
                    # If current spin is up, flip down with prob e^(-|dE|/T)
                    self.MetropolisProbUp[1, nUp] = 1. - \
                        scipy.exp(-(eDown - eUp) / T)
                else:  # Up spin unstable
                    # If current spin is down, flip up with prob e^(-|dE|/T)
                    self.MetropolisProbUp[
                        0, nUp] = scipy.exp(-(eUp - eDown) / T)
                    # If current spin is up, flip down
                    self.MetropolisProbUp[1, nUp] = 0.
            else:
                if eDown > eUp:  # Down spin unstable
                    # If current spin is down, flip up
                    self.MetropolisProbUp[0, nUp] = 1.
                    # If current spin is up, leave alone
                    self.MetropolisProbUp[1, nUp] = 0.
                elif eDown < eUp:  # Up spin unstable
                    # If current spin is down, leave alone
                    self.MetropolisProbUp[0, nUp] = 0.
                    # If current spin is up, flip down
                    self.MetropolisProbUp[1, nUp] = 1.
        # Set up Wolff algorithm
        if T == 0:
            self.p = 0.
        else:
            self.p = 1.0 - scipy.exp(-2. * J / T)

    def GetTemperature(self):
        return self.privateTemperature

    def GetField(self):
        return self.privateField

    def NeighborsUp(self, i, j):
        """
        Sums self.lattice at four neighbor sites, modulo self.N
        """
        ip1 = (i + 1) % self.N
        im1 = (i - 1) % self.N
        jp1 = (j + 1) % self.N
        jm1 = (j - 1) % self.N
        return (self.lattice[ip1][j] + self.lattice[im1][j]
                + self.lattice[i][jp1] + self.lattice[i][jm1])

    def SweepHeatBath(self, nTimes=1):
        """
        Slow variant (for debugging):
        For each time in range(ntimes):
            For n in range(N):
                Pick a random spin (i,j)
                Find NeighborsUp(i,j)
                Find the probability heatBathProbUp that the spin will be up
                Create a random number r in (0,1]
                if rand < heatBathProbUp, set spin lattice[i][j]=1
        #
        Fast variant:
        For each time in range(ntimes):
            Creates N random (i,j) pairs
            Creates N random numbers in (0,1]
                (note: use 1-scipy.random.random() to avoid zero)
            if rand < heatBathProbUp for NeighborsUp(i,j)
                set spin lattice[i][j]=1
            else set it to zero
        """
        for time in range(nTimes):
            iArr = scipy.random.randint(0, self.N, self.N * self.N)
            jArr = scipy.random.randint(0, self.N, self.N * self.N)
            randomArr = 1. - scipy.random.random(self.N * self.N)
            for i, j, rand in zip(iArr, jArr, randomArr):
                if rand < self.heatBathProbUp[self.NeighborsUp(i, j)]:
                    self.lattice[i, j] = 1
                else:
                    self.lattice[i, j] = 0

    def SweepMetropolis(self, nTimes=1, updates_per_sweep=None):
        """
        For each time in range(ntimes):
            Creates N random (i,j) pairs
            Creates N random numbers in (0,1]
            if rand < MetropolisProbUp for current spin, NeighborsUp(i,j)
                    set spin lattice[i][j]=1
            else set it to zero

        if updates_per_time is given, do overwrites the N**2 updates
        per sweep
        """
        if updates_per_sweep is None:
            updates_per_sweep = self.N * self.N

        for time in range(nTimes):
            iArr = scipy.random.randint(0, self.N, updates_per_sweep)
            jArr = scipy.random.randint(0, self.N, updates_per_sweep)
            randomArr = 1. - scipy.random.random(updates_per_sweep)
            for i, j, rand in zip(iArr, jArr, randomArr):
                if rand < self.MetropolisProbUp[self.lattice[i][j],
                                                self.NeighborsUp(i, j)]:
                    self.lattice[i][j] = 1
                else:
                    self.lattice[i][j] = 0

    def WolffMoveRecursive(self):
        """
        Slow, recursive variant of Wolff move
        #
        Pick a random spin; remember its direction
        Flip it
        Call FlipNeighbors; add one to its result
        return spinsFlipped
        """
        i = scipy.random.randint(0, self.N)
        j = scipy.random.randint(0, self.N)
        oldSpin = self.lattice[i, j]
        self.lattice[i, j] = (self.lattice[i, j] + 1) % 2
        spinsFlipped = 1 + self.FlipNeighbors(i, j, oldSpin)
        return spinsFlipped

    def FlipNeighbors(self, i, j, oldSpin):
        """
        Used by WolffMoveRecursive
        #
        Initialize spinsFlipped to zero
        For m, n in neighbors of i, j:
           if lattice[m][n]==oldSpin and random()<p
              flip spin; add one to spinsFlipped
              Call FlipNeighbors on (m,n); add to spinsFlipped
        return spinsFlipped
        """
        spinsFlipped = 0
        ip1 = (i + 1) % self.N
        im1 = (i - 1) % self.N
        jp1 = (j + 1) % self.N
        jm1 = (j - 1) % self.N
        neighbors = [(ip1, j), (im1, j), (i, jp1), (i, jm1)]
        for m, n in neighbors:
            if self.lattice[m][n] == oldSpin:
                if scipy.random.random() < self.p:
                    self.lattice[m][n] = (self.lattice[m][n] + 1) % 2
                    spinsFlipped += 1 + self.FlipNeighbors(m, n, oldSpin)
        return spinsFlipped

    def WolffMove(self):
        """
        Faster, list-based Wolff move.
        #
        Pick a random spin; remember its direction as oldSpin
        Push it onto a list "toFlip" of spins to flip
        Set spinsFlipped = 0
        While there are spins left in toFlip
           Remove the first spin
           If it has not been flipped in between
              Flip it
              Add one to spinsFlipped
              For each of its neighbors
                  if the neighbor is in the oldSpin direction
                  with probability p, put it on the stack
        Return spinsFlipped
        """
        i = scipy.random.randint(0, self.N)
        j = scipy.random.randint(0, self.N)
        oldSpin = self.lattice[i, j]
        toFlip = [(i, j)]
        spinsFlipped = 0
        while len(toFlip) > 0:
            i, j = toFlip.pop(0)
            # Check if flipped in between
            if self.lattice[i, j] == oldSpin:
                self.lattice[i, j] = (self.lattice[i, j] + 1) % 2
                spinsFlipped += 1
                ip1 = (i + 1) % self.N
                im1 = (i - 1) % self.N
                jp1 = (j + 1) % self.N
                jm1 = (j - 1) % self.N
                neighbors = [(ip1, j), (im1, j), (i, jp1), (i, jm1)]
                for m, n in neighbors:
                    if self.lattice[m, n] == oldSpin:
                        if scipy.random.random() < self.p:
                            toFlip.append((m, n))
        return spinsFlipped

    def SweepWolff(self, nTimes=1, partialSweep=0):
        """
        Do nTimes sweeps of the Wolff algorithm, returning partialSweep
        (1) The variable partialSweep is the number of `extra' spins flipped
        in the previous Wolff cluster moved that belong to the current sweep.
        (2) A sweep is comprised of Wolff cluster moves until at least
        N*N-partialSweep spins have flipped. (Just add the spinsFlipped
        from WolffMove to partialSweep, while partialSweep < N*N, the
        new partialSweep is the current one minus N*N.)
        (3) Return the new value of partialSweep after nTimes sweeps.
        (4) You might print an error message if the field is not zero
        """
        if self.GetField() != 0.:
            print("Field will be ignored by Wolff algorithm")
        for time in range(nTimes):
            while partialSweep < self.N * self.N:
                partialSweep += self.WolffMove()
            partialSweep = partialSweep - (self.N * self.N)
        return partialSweep


# Copyright (C) Cornell University
# All rights reserved.
# Apache License, Version 2.0
