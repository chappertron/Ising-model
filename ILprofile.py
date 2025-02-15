import time  # NB if running python < 3.3 use time.clock instead of time.process_time
import cProfile
import IsingLattice as il


# use a relatively big lattice of 25x25 so that we get more accurate timing data
n_rows = 25
n_cols = 25

lattice = il.IsingLattice(n_rows, n_cols)
# record the time at which we start running
start_time = time.process_time()
# do 2000 monte carlo steps
with cProfile.Profile() as prof:
    for i in range(2000):
        lattice.montecarlostep(1.0)
# record the time at which we stop running
end_time = time.process_time()

# work out how many seconds the loop took, and print it
elapsed_time = end_time - start_time
print("2000 steps took {} s".format(elapsed_time))

prof.print_stats()
prof.dump_stats("ising.prof")
