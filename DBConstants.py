class DBConstants:
    register_user      = 'INSERT INTO Utilizador (nome, email,password,idCarteira,dataNascimento,nif,isAdmin,isEspecialista) VALUES ((%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s));'
    add_wallet         = 'INSERT INTO Carteira (saldoCarteira) VALUES(0.00);'
    get_wallet         = 'SELECT idCarteira FROM Utilizador WHERE idUser=%s;'
    update_wallet      = 'UPDATE Carteira SET saldoCarteira=%s WHERE idCarteira=%s;'
    get_log_info       = 'SELECT nome, email, password, idUser, isAdmin, isEspecialista FROM Utilizador WHERE email=(%s);'
    add_team           = 'INSERT INTO EquipasPorJogo(nomeEquipa, idJogo, Odd, jogaEmCasa) VALUES((%s),(%s),(%s),(%s));'    
    get_sports         = 'SELECT DISTINCT nomeDesporto FROM Jogo;'
    get_by_sport       = 'SELECT idJogo FROM Jogo WHERE nomeDesporto = (%s) AND suspenso=0 AND finalizado=0 AND NOW() < dataJogo;'
    get_by_sport_wSusp = 'SELECT idJogo FROM Jogo WHERE nomeDesporto = (%s) AND finalizado=0;'
    suspende_game      = 'UPDATE Jogo SET suspenso=%s WHERE idJogo=%s;'
    elimina_game       = 'DELETE FROM Jogo WHERE idJogo=%s;'
    get_game_info      = 'SELECT nomeEquipa, Odd, jogaEmCasa FROM EquipasPorJogo WHERE idJogo = (%s);'
    get_balance        = 'SELECT saldoCarteira FROM Carteira WHERE idCarteira = (SELECT idCarteira FROM Utilizador WHERE idUser=%s);'
    create_promotion   = 'INSERT INTO Promoção(idJogo, percentagemAumento) Values(%s,%s);'
    boosted_odds       = 'UPDATE EquipasPorJogo SET Odd = Odd * %s WHERE idJogo=%s;'
    get_promotion      = 'SELECT idPromoçao, percentagemAumento, idJogo FROM Promoção WHERE idPromoçao=%s'
    get_promotions     = 'SELECT * FROM Promoção'
    remove_promotion   = 'DELETE FROM Promoção WHERE idPromoçao=%s;'
    get_history_bets   = 'SELECT idAposta, dataAposta, valorApostado FROM Aposta WHERE idUser=%s;'
    get_history_trans  = 'SELECT idTransação, dataTransação, descricao, valorTransação, saldoAntes FROM Transação WHERE idUser=%s;'
    get_balance        = 'SELECT saldoCarteira FROM Carteira WHERE idCarteira = (SELECT idCarteira FROM Utilizador WHERE idUser=%s);'
    reg_transaction    = 'INSERT INTO Transação(saldoAntes,valorTransação,idUser,descricao) VALUES(%s,%s,%s,%s)'
    reg_aposta         = 'INSERT INTO Aposta(idUser, valorApostado, numeroJogos) VALUES(%s,%s,%s)'
    update_nmr_jogos   = 'UPDATE Aposta SET numeroJogos=numeroJogos-1 WHERE idAposta=%s;'
    get_nmr_jogos      = 'SELECT numeroJogos FROM Aposta WHERE idAposta=%s'
    add_game_to_bet    = 'INSERT INTO JogoPorAposta(idAposta,idJogo,odd,resultadoApostado) VALUES(%s,%s,%s,%s)'
    get_odd_by_game    = 'SELECT Odd FROM EquipasPorJogo WHERE idJogo=%s AND nomeEquipa=%s'
    create_game        = 'INSERT INTO Jogo(idJogo, nomeDesporto, dataJogo) VALUES(%s, %s, %s);'
    add_team           = 'INSERT INTO EquipasPorJogo(nomeEquipa, idJogo, Odd, jogaEmCasa) VALUES(%s,%s,%s,%s);'
    get_last_update    = 'SELECT lastUpdate FROM Jogo WHERE idJogo=%s;'
    get_game_by_ID     = 'SELECT idJogo FROM Jogo WHERE idJogo=%s;'
    get_game_by_day    = 'SELECT dataJogo, idJogo FROM Jogo WHERE nomeDesporto=%s;'
    get_games_calendar = 'SELECT dataJogo FROM Jogo WHERE nomeDesporto=%s;'
    get_distinct_ganho = 'SELECT DISTINCT ganho FROM JogoPorAposta WHERE idAposta=%s;'
    set_aposta         = 'UPDATE Aposta SET ApostaGanha=%s WHERE idAposta=%s;'
    get_userid_by_bet  = 'SELECT idUser, valorApostado FROM Aposta WHERE idAposta=%s;'
    update_odds        = 'UPDATE EquipasPorJogo SET Odd=%s WHERE idJogo=%s AND nomeEquipa=%s;'
    update_pass_field  = 'UPDATE Utilizador SET password=%s WHERE idUser=%s;'
    update_nome_field  = 'UPDATE Utilizador SET nome=%s WHERE idUser=%s;'
    get_teams_by_game  = 'SELECT idJogo, nomeEquipa, Odd, jogaEmCasa from EquipasPorJogo WHERE idJogo=%s;'
    get_game_date      = 'SELECT dataJogo FROM Jogo WHERE idJogo=%s;'
    get_game_state     = 'SELECT finalizado FROM Jogo WHERE idJogo=%s;'
    set_game_state     = 'UPDATE Jogo SET finalizado=%s WHERE idJogo=%s;'
    set_winner         = 'UPDATE Jogo SET resultado=%s WHERE idJogo=%s;'
    #get_bets          = 'SELECT idAposta FROM JogoPorAposta WHERE idJogo=%s AND resultadoApostado=%s'
    #get_bets_no_res   = 'SELECT idAposta FROM JogoPorAposta WHERE idJogo=%s AND resultadoApostado!=%s'
    set_bet_winner     = 'UPDATE JogoPorAposta SET ganho=1 WHERE idJogo=%s AND resultadoApostado=%s;'
    idJogos_aposta     = 'SELECT idJogo FROM JogoPorAposta WHERE idAposta=%s;'
    get_bets_winner    = 'SELECT idAposta FROM JogoPorAposta WHERE idJogo=%s AND resultadoApostado=%s;'
    set_bet_loser      = 'UPDATE JogoPorAposta SET ganho=0 WHERE idJogo=%s AND resultadoApostado!=%s;'
    get_bets_loser     = 'SELECT idAposta FROM JogoPorAposta WHERE idJogo=%s AND resultadoApostado!=%s;'
    get_special_users  = 'SELECT email, isAdmin, isEspecialista FROM Utilizador WHERE isAdmin=1 OR isEspecialista=1;'
    get_user           = 'SELECT idUser FROM Utilizador WHERE idUser=%s;'
    remove_special_user= 'DELETE FROM Utilizador WHERE idUser=%s;'
    ganho_por_aposta   = 'SELECT jogoporaposta.ganho FROM jogoporaposta JOIN Aposta ON aposta.idAposta = jogoporaposta.idAposta WHERE aposta.idAposta=%s;'
    get_game_result    = 'SELECT resultado FROM Jogo WHERE idJogo=%s AND finalizado=1;'
    get_montante       = 'SELECT valorApostado FROM Aposta WHERE idAposta=%s;'
    get_aposta_result  = 'SELECT ApostaGanha FROM Aposta WHERE idAposta=%s;'
    update_odd_total   = 'UPDATE Aposta SET oddTotal=%s WHERE idAposta=%s;'
    get_odd_total      = 'SELECT oddTotal FROM Aposta WHERE idAposta=%s;'
    add_notificacao    = 'INSERT INTO Notificação(idUser,Título,Texto) VALUES(%s,%s,%s);'
    get_notificacao    = 'SELECT Título, Texto FROM Notificação WHERE idUser = %s or idUser=-1'
    close_game         = 'UPDATE Jogo SET resultado=%s WHERE idJogo=%s'
    close_game_t       = 'UPDATE Jogo SET finalizado=1 WHERE idJogo=%s'
