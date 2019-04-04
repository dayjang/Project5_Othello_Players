from Board_Play import * 



players_dic = {'random': random_strategy, 'maximizer': maximizer(WeightMatrixScore), 'minimax_depth2': minimax_searcher(2,WeightMatrixScore) , 'minimax_depth3': minimax_searcher(3,WeightMatrixScore)  , 'minimax_depth4': minimax_searcher(4,WeightMatrixScore)  ,' minimax_depth5' : minimax_searcher(5,WeightMatrixScore) }


def ChoosePlayers():
	print("Let's play Othello/Reversi :-)")
	print("Black ALWAYS go FIRST")
	print("Available players: random, maximizer, minimax_depth2, minimax_depth3, minimax_depth4, minimax_depth5, minimax_alphabeta_depth2, minimax_alphabeta_depth3 ..... ")
	bl_strat = input("Choose a black player: ")
	wh_strat = input("Choose a white player: ")

	return bl_strat, wh_strat



if __name__ == '__main__':
	try: 
		b, w = ChoosePlayers()
		board, score = play(players_dic[b],players_dic[w])
 	except: 
 		"ERROR OCCURED"
 		"Please check you input players correctly"


def simulation(n_simul, black_strat_input, white_strat_input):
    print('start!')
    black, white = options[black_strat_input], options[white_strat_input]
    result=[]
    start_time = time.time()

    for i in range(n_simul):
        result.append(main_new(black, white))

    black_win = np.sum(np.array(result)=='BLACK')/n_simul
    white_win = np.sum(np.array(result)=='WHITE')/n_simul
    tie = np.sum(np.array(result)=='TIE')/n_simul
    print('black_strategy: {}, white_strategy: {}'.format(black_strat_input, white_strat_input))

    elapsed_time = time.time() - start_time
    # elapsed_time2 = time.strftime("%H:%M:%S", time.gmtime(elapsed_time/n_simul))
    print('#_of_simulation:{}, black_win_%: {}, white_win_%: {}, tie_%: {} , elapsed_time_tot: {}'.format(n_simul,black_win,white_win,tie,elapsed_time))

    return n_simul,black_win,white_win,tie,elapsed_time


simulation(1, 'max-weighted-diff', 'ab-weighted-diff5')

