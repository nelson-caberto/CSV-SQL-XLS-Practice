import sqlite3
import csv
import sys

def createDBConnection(db_file):
	"""
	returns handle for accessing db as a file or in memory
	"""
	
	try:
		dbConnection = sqlite3.connect(db_file)
		return dbConnection
	except sqlite3.Error as e:
		print(e)
	except Exception as e:
		print(e)
	return None

def initializeDatabase(db_file=':memory:'):
	"""
	creates a new database or loads existing database
	"""

	dbConnection = createDBConnection(db_file)
	
	if dbConnection is None:
		sys.exit('Failed to create dbConnection.')
	else:
		dbCursor = dbConnection.cursor()
		
	sqlSTMT = """
	CREATE TABLE IF NOT EXISTS a (
		id integer PRIMARY KEY,
		int3 integer NOT NULL,
		char7 text NOT NULL,
		char2 text NOT NULL,
		int4a integer NOT NULL,
		float8 float NOT NULL,
		int4b integer NOT NULL );
	"""
	
	try:
		dbCursor.execute(sqlSTMT)
	except sqlite3.Error as e:
		sys.exit(f'Database Error: {e} on {sqlSTMT}')
	except Exception as e:
		sys.exit(f'Database Exception: {e} on {sqlSTMT}')
	
	return dbConnection

def csvDBEntry(dbCursor, csv_file, sqlSTMT):
	with open(csv_file, mode='r') as file:
		csv_reader = csv.reader(file, delimiter=',')
		
		for row in csv_reader:
			try:
				dbCursor.execute(sqlSTMT, row)
			except sqlite3.Error as e:
				print(f'Database error: {e} on {row}')
				continue
			except Exception as e:
				print(f'Exception in _query: {e} on {row}')
				continue

def writeCell(column, row, int4a, results, totals, float8s):
	lIndex = 306 - ((column-1) * 18 + row)
	if 4074071952668972172536891376818756322102936787331872501272280898708762599526673412366794752&(1<<(lIndex))!=0: return 'int4a'
	if 1018517988167243043134222844204689080525734196832968125318070224677190649881668353091698688&(1<<(lIndex))!=0: return f'{int4a}'
	if 15541351137805832567355695254588151253139254712417116170014499277911234281641667985408     &(1<<(lIndex))!=0: return 'float8'
	if 3885337784451458141838923813647037813284813678104279042503624819477808570410416996352      &(1<<(lIndex))!=0: return f'{float8s[0][2]} and under'
	if 1942668892225729070919461906823518906642406839052139521251812409738904285205208498176      &(1<<(lIndex))!=0: return f'{float8s[1][1]} - {float8s[1][2]}'
	if 971334446112864535459730953411759453321203419526069760625906204869452142602604249088       &(1<<(lIndex))!=0: return f'{float8s[2][1]} - {float8s[2][2]}'
	if 485667223056432267729865476705879726660601709763034880312953102434726071301302124544       &(1<<(lIndex))!=0: return f'{float8s[3][1]} - {float8s[3][2]}'
	if 242833611528216133864932738352939863330300854881517440156476551217363035650651062272       &(1<<(lIndex))!=0: return f'{float8s[4][1]} - {float8s[4][2]}'
	if 121416805764108066932466369176469931665150427440758720078238275608681517825325531136       &(1<<(lIndex))!=0: return f'{float8s[5][1]} - {float8s[5][2]}'
	if 60708402882054033466233184588234965832575213720379360039119137804340758912662765568        &(1<<(lIndex))!=0: return f'{float8s[6][1]} - {float8s[6][2]}'
	if 30354201441027016733116592294117482916287606860189680019559568902170379456331382784        &(1<<(lIndex))!=0: return f'{float8s[7][1]} - {float8s[7][2]}'
	if 15177100720513508366558296147058741458143803430094840009779784451085189728165691392        &(1<<(lIndex))!=0: return f'{float8s[8][1]} - {float8s[8][2]}'
	if 7588550360256754183279148073529370729071901715047420004889892225542594864082845696         &(1<<(lIndex))!=0: return f'{float8s[9][1]} - {float8s[9][2]}'
	if 3794275180128377091639574036764685364535950857523710002444946112771297432041422848         &(1<<(lIndex))!=0: return f'{float8s[10][1]} - {float8s[10][2]}' 
	if 1897137590064188545819787018382342682267975428761855001222473056385648716020711424         &(1<<(lIndex))!=0: return f'{float8s[11][1]} and over'
	if 948568795032094272909893509191171341133987714380927500611236528192824358010355712          &(1<<(lIndex))!=0: return 'Title'
	if 474284397516047136454946754595585670566993857190463750305618264096412179005177856          &(1<<(lIndex))!=0: return 'char7'
	if 237142198758023568227473377297792835283496928595231875152809132048206089502588928          &(1<<(lIndex))!=0: return 'char7[0]'
	if 59285549691231328643565985271306897786443488511920746031244879650842153431597056           &(1<<(lIndex))!=0: return 'char2[0]'
	if 29642774844752946028434172162224104410437116074403984394101141506025761187823616           &(1<<(lIndex))!=0: return 'A'
	if 29635537839175613766220198975661061416196286700362381858848675407025266617221120           &(1<<(lIndex))!=0: result = results[int4a]['A']['A']
	if 226156424291633194186662080095093570031234850783218890131180822006576709632                &(1<<(lIndex))!=0: return 'char2[1]'
	if 113078212145816597093331040047546785012958969400039613319782796882727665664                &(1<<(lIndex))!=0: return 'B'
	if 113050605160429434838181301024097676911149164964150931773562146785832468480                &(1<<(lIndex))!=0: result = results[int4a]['B']['A']
	if 3450873173395281893717377931138512726225554486085193277581262111899648                     &(1<<(lIndex))!=0: return 'Non/char7[0]'
	if 862718293348820473429344482784630840012380191353044127009436088664064                      &(1<<(lIndex))!=0: return 'char7[1]'
	if 431359146674410236714672241392314090778194310760649159697657763987456                      &(1<<(lIndex))!=0: return 'C'
	if 431253834382741679527974323364630420345875415665248610586403453009920                      &(1<<(lIndex))!=0: result = results[int4a]['A']['B']
	if 3291009114642412084309938365114711151170273557102371700322861056                           &(1<<(lIndex))!=0: return 'char7[2]'
	if 1645504557321206042154969182557350504982735865633579863348609024                           &(1<<(lIndex))!=0: return 'D'
	if 1645102822810141294586083692034265214332105314885134165139783680                           &(1<<(lIndex))!=0: result = results[int4a]['A']['C']
	if 12554203470773361527671578846415371517830938557061659623424                                &(1<<(lIndex))!=0: return 'char7[3]'
	if 6277101735386680763835789423207666416102355444464034512896                                 &(1<<(lIndex))!=0: return 'E'
	if 6275569239845814874977431076180516106918736705341850910720                                 &(1<<(lIndex))!=0: result = results[int4a]['A']['D']
	if 47890485652059026823698344598447309562038187244650496                                      &(1<<(lIndex))!=0: return 'char7[4]'
	if 23945242826029513411849172299223580994042798784118784                                      &(1<<(lIndex))!=0: return 'F'
	if 23939396819480189800176357559892715861964175053946880                                      &(1<<(lIndex))!=0: result = results[int4a]['A']['E']
	if 182687704666362864775460604089535940406944989184                                           &(1<<(lIndex))!=0: return 'char7[5]'
	if 91343852333181432387730302044767688728495783936                                            &(1<<(lIndex))!=0: return 'G'
	if 91321551587982901764588766326495040366989803520                                            &(1<<(lIndex))!=0: result = results[int4a]['A']['F']
	if 696898287454081973172991196020263444545536                                                 &(1<<(lIndex))!=0: return 'char7[6]'
	if 348449143727040986586495598010130648530944                                                 &(1<<(lIndex))!=0: return 'H'
	if 348364073135310751970629754358272706478080                                                 &(1<<(lIndex))!=0: result = results[int4a]['A']['G']
	if 1329227995784915872903807060280344576                                                      &(1<<(lIndex))!=0: return 'I'
	if 1328903477231257446177023904259768320                                                      &(1<<(lIndex))!=0: result = results[int4a]['B']['B']
	if 5070602400912917605986812821504                                                            &(1<<(lIndex))!=0: return 'J'
	if 5069364460873632225711913697280                                                            &(1<<(lIndex))!=0: result = results[int4a]['B']['C']
	if 19342813113834066795298816                                                                 &(1<<(lIndex))!=0: return 'K'
	if 19338090747351197150085120                                                                 &(1<<(lIndex))!=0: result = results[int4a]['B']['D']
	if 73786976294838206464                                                                       &(1<<(lIndex))!=0: return 'L'
	if 73768961896328724480                                                                       &(1<<(lIndex))!=0: result = results[int4a]['B']['E']
	if 281474976710656                                                                            &(1<<(lIndex))!=0: return 'M'
	if 281406257233920                                                                            &(1<<(lIndex))!=0: result = results[int4a]['B']['F']
	if 1073741824                                                                                 &(1<<(lIndex))!=0: return 'N'
	if 1073479680                                                                                 &(1<<(lIndex))!=0: result = results[int4a]['B']['G']
	if 29635650890212029675146877239810688379576640920336595789344087638804894626611200           &(1<<(lIndex))!=0: return result[row]
	if 8192                                                                                       &(1<<(lIndex))!=0: return 'Total Col A-N'
	if 4096                                                                                       &(1<<(lIndex))!=0: return 'O'
	if 4095                                                                                       &(1<<(lIndex))!=0: total = totals[int4a]
	if 4095                                                                                       &(1<<(lIndex))!=0: return total[row]
	return ''
