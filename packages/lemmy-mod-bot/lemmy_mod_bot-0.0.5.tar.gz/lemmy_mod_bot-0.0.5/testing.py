from matrix import send_message_to_matrix
import credentials

send_message_to_matrix(credentials.matrix_server, credentials.matrix_account, credentials.matrix_password, credentials.matrix_room_id,"bar")
