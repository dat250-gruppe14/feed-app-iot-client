from IoTVoter import IoTVoter

if __name__ == '__main__':
	from board_config import board_config

	IoTVoter(board_config)

	message = input('Press enter to quit')

