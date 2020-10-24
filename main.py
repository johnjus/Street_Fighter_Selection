fighters = [
	["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
	["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
]
moves =  []

def street_fighter_selection(fighters, initial_position, moves):
    pos = [0,0]
    ssf = []
    if len(moves) == 0:
      return moves
    else:
      for move in moves:
        if move == 'up':

          if pos[0] != 0:
            pos[0] = pos[0]-1
            ssf.append(fighters[pos[0]][pos[1]])
          else:
            ssf.append(fighters[pos[0]][pos[1]])


        elif move == 'down':

          if pos[0] == 0:          
            pos[0] = pos[0]+1
            ssf.append(fighters[pos[0]][pos[1]])
          else:       
            ssf.append(fighters[pos[0]][pos[1]])


        elif move == 'right':
          if pos[1] == len(fighters[1])-1:
            pos[1] = 0
            ssf.append(fighters[pos[0]][pos[1]])
          else:
            pos[1] = pos[1] +1
            ssf.append(fighters[pos[0]][pos[1]])


        elif move == 'left':
          if pos[1] == 0:
            pos[1] = len(fighters[1])-1
            ssf.append(fighters[pos[0]][pos[1]])
          else:
            pos[1] = pos[1] -1
            ssf.append(fighters[pos[0]][pos[1]])
      return ssf


print(street_fighter_selection(fighters,(0,0), moves))