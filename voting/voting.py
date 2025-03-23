def tie_break_function(preferences, sc, tie_break):
    """
    Resolves ties by selecting the candidate with the highest preference from the tie-breaking agent.
    """
    #find the maximum score among the candidates
    max_sc = max(sc.values())
    #list storing candidates with the highest score
    final_candidates = []

    #find all candidates with the highest score
    for candidate in preferences.candidates():
        if sc[candidate] == max_sc:
            final_candidates.append(candidate)

    #if only one candidate has the highest score, return it as the winner
    if len(final_candidates) == 1:
        return final_candidates[0]
    else:
        #for multiple candidates, break the tie using the tie-breaking agent's preference
        tb_score={candidate: preferences.get_preference(candidate, tie_break) for candidate in final_candidates}
        for candidate in final_candidates:
            if tb_score[candidate] == min(tb_score.values()):
                return candidate

def dictatorship(preferences, agent):
    """ 
    Impliments the dictatorship rule for selecting a winner based on a specific agent's preferences.
    """
    #Check if agent is a valid voter
    voters = preferences.voters()
    candidates = preferences.candidates()
    if agent not in voters:
        raise ValueError("Invalid agent.")
    #Find the candidate ranked first (the one with rank 0) by the dictator
    for i in candidates:
        if preferences.get_preference(i, agent) == 0:
            return i

def scoring_rule(preferences, score_vector, tie_break): 
    """
    Impliments the scoring rule to find the winner, based on the scoring vector.
    """
    #get the list of voters and candidates
    voters = preferences.voters()
    candidates = preferences.candidates()
    #sort the score_vector in the reverse order to assign the highest score to the most preferred alternative of the agent
    score_vector.sort(reverse=True)

    #create a dictionary for storing the total scores for each candidate
    sc={c:0 for c in preferences.candidates()}
    #loop through voters and candidates
    for voter in voters:
        for candidate in candidates:
            #add the score corresponding to candidate's rank for each voter, using the values in the score_vector
            sc[candidate] += score_vector[preferences.get_preference(candidate, voter)]
    
    #use the tie-breaking rule to distinguish between alternatives with the same score
    return tie_break_function(preferences, sc, tie_break)

def plurality(preferences, tie_break):
    """
    Impliments the plurality rule to find the winner, based on the position of the agents' preference orderings.
    """
    #get the list of voters and candidates
    voters = preferences.voters()
    candidates = preferences.candidates()
    #create a dictionary for storing the scores for each candidate, based on the rule
    sc={c:0 for c in preferences.candidates()}
    #loop through voters and candidates
    for voter in voters:
        for candidate in candidates:
            if preferences.get_preference(candidate, voter) == 0:
                #find the voter's top choice and add 1 to the score of that candidate
                sc[candidate] += 1

     
    #use the tie-breaking rule to decide the winner if there's a tie      
    return tie_break_function(preferences, sc, tie_break)

def  veto(preferences, tie_break):
    """
    Impliments the veto rule to assing points in order to find the winner.
    """
    #get the list of voters and candidates
    voters = preferences.voters()
    candidates = preferences.candidates()
    #create a dictionary for storing the scores for each candidate, based on the rule
    sc={c:0 for c in preferences.candidates()}
    #loop through voters and candidates
    for voter in voters:
        for candidate in candidates:
            #find the candidates not ranked last by the voters and add a point to to those candidates
            if preferences.get_preference(candidate, voter) != (len(candidates)-1):
                sc[candidate] += 1

    #use the tie-breaking rule to decide the winner if there's a tie      
    return tie_break_function(preferences, sc, tie_break)

def  borda(preferences, tie_break):
    """
    Impliments the borda rule to assing points in order to find the winner.
    """
    #get the list of voters and candidates
    voters = preferences.voters()
    candidates = preferences.candidates()
    #create a dictionary for storing the scores for each candidate, based on the rule
    sc={c:0 for c in preferences.candidates()}
    #loop through voters and candidates
    for voter in voters:
        for candidate in candidates:
            #assign a score based on the candidate's position in the voter's ranking, with higher positions getting higher scores
            sc[candidate]+=len(candidates)-preferences.get_preference(candidate, voter)-1

    #use the tie-breaking rule to decide the winner if there's a tie        
    return tie_break_function(preferences, sc, tie_break)

def STV (preferences, tie_break):
    """
    Implements the STV rule by eliminating candidates with the fewest first-place votes until one remains.
    """
    #get the list of voters
    voters = preferences.voters()
    #list of candidates still remaining
    remaining=list(preferences.candidates())
    while len(remaining)>1:
        #create a dictionary for storing the scores for each candidate, based on the rule
        sc={c:0 for c in remaining}
        #check each voter's top choice and update the candidate’s score
        for voter in voters:
            for candidate in remaining:
                #if candidate is ranked first
                if preferences.get_preference(candidate, voter) == 0:
                    sc[candidate] += 1
        #check if there's a clear candidate to eliminate
        if min(sc.values()) != max(sc.values()):
            #remove all candidates with the fewest first-place votes
            for candidate in remaining:
                if sc[candidate] == min(sc.values()):
                    remaining.remove(candidate)
        else:
            return tie_break_function(preferences, sc, tie_break)
    #return the last remaining candidate
    return remaining[0]
