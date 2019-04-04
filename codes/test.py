from Board_Play import * 

players_dic = {'random': random_strategy, 'maximizer': maximizer(WeightMatrixScore), 'minimax_depth2': minimax_searcher(2,WeightMatrixScore) , 'minimax_depth3': minimax_searcher(3,WeightMatrixScore)  , 'minimax_depth4': minimax_searcher(4,WeightMatrixScore)  ,' minimax_depth5' : minimax_searcher(5,WeightMatrixScore) }


def ChoosePlayers():
	print("Let's play Othello/Reversi :-)")
	print("Black ALWAYS go FIRST")
	print("Available players: random, maximizer, minimax_depth2, minimax_depth3, minimax_depth4, minimax_depth5, minimax_alphabeta_depth2, minimax_alphabeta_depth3 ..... ")
	bl_strat = input("Choose a black player: ")
	wh_strat = input("Choose a white player: ")

	return bl_strat, wh_strat



def main(b,w)
	try: 
		# b, w = ChoosePlayers()
		board, score = play(players_dic[b],players_dic[w])
 	except: 
 		"ERROR OCCURED"
 		"Please check you input players correctly"
    
    print('Final score:', score)
    print(PrintBoard(board))
    print('Winner is..?')

    if score>0:
        print('BLACK')
        return 'BLACK'
    elif score<0:
        print('WHITE')
        return 'WHITE'
    else:
        print('TIE')
        return 'TIE'



def simulation(n_simul):
    print('start!')
    b, w = ChoosePlayers()
    result=[]
    
    start_time = time.time()

    for i in range(n_simul):
        result.append(main_new(b, w))

    black_win = np.sum(np.array(result)=='BLACK')/n_simul
    white_win = np.sum(np.array(result)=='WHITE')/n_simul
    tie = np.sum(np.array(result)=='TIE')/n_simul
    print('black_strategy: {}, white_strategy: {}'.format(black_strat_input, white_strat_input))

    elapsed_time = time.time() - start_time

    print('#_of_simulation:{}, black_win_%: {}, white_win_%: {}, tie_%: {} , elapsed_time_tot: {}'.format(n_simul,black_win,white_win,tie,elapsed_time))

    return n_simul,black_win,white_win,tie,elapsed_time



if __name__ == '__main__':
    n_simulation=int(input(Number of simulation of the game))
    simulation(n_simulation)





