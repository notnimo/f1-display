drivers: list[str] = ['Adrian Sutil', 'Alexander Albon', 'Alexander Rossi', 'Andre Lotterer', 'Antonio Giovinazzi', 'Brendon Hartley', 'Bruno Senna', 'Carlos Sainz', 'Charles Leclerc', 'Charles Pic', 'Christian Klien', 'Daniel Ricciardo', 'Daniil Kvyat', 'Esteban Ocon', 'Felipe Massa', 'Felipe Nasr', 'Fernando Alonso', 'Gabriel Bortoleto', 'George Russell', 'Giedo van der Garde', 'Heikki Kovalainen', 'Isack Hadjar', 'Jack Doohan', 'Jaime Alguersuari', 'Jarno Trulli', 'Jean-Eric Vergne', 'Jenson Button', 'Jolyon Palmer', 'Jules Bianchi', 'Kamui Kobayashi', 'Karun Chandhok', 'Kevin Magnussen', 'Kimi Antonelli', 'Lance Stroll', 'Lando Norris', 'Lewis Hamilton', 'Liam Lawson', 'Logan Sargeant', 'Lucas di Grassi', 'Ma Qing Hua', 'Marcus Ericsson', 'Mark Webber', 'Max Chilton', 'Max Verstappen', 'Michael Schumacher', 'Mick Schumacher', 'Narain Karthikeyan', 'Nicholas Latifi', 'Nick Heidfeld', 'Nico Hulkenberg', 'Nico Rosberg', 'Nikita Mazepin', 'Nyck de Vries', 'Oliver Bearman', 'Oscar Piastri', 'Pascal Wehrlein', 'Pastor Maldonado', 'Paul di Resta', 'Pedro de la Rosa', 'Pierre Gasly', 'Rio Haryanto', 'Robert Kubica', 'Robert Shwartzman', 'Roberto Merhi', 'Romain Grosjean', 'Rubens Barrichello', 'Sakon Yamamoto', 'Sebastian Vettel', 'Sebastien Buemi', 'Sergio Perez', 'Stoffel Vandoorne', 'Timo Glock', 'Valtteri Bottas', 'Vitaly Petrov', 'Vitantonio Liuzzi', 'Will Stevens', 'Yuki Tsunoda', 'Zhou Guanyu']

def getDriversList() -> list[str]:
  return drivers

def getDriverWithId(id: int) -> str:
  return drivers[id]

def getIdOfDriver(driver: str) -> int:
  return drivers.index(driver)

if __name__ == "__main__":
  print(sorted(getDriversList()))