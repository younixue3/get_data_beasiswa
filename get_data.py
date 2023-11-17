# from datetime import datetime
#
# import pandas as pd
# import requests
# import numpy
# import json
# import csv
#
# # formData = {'username': 'shs500', 'password': 'Ilkomerz2007*'}
# # jwt_get = requests.post('https://api.umkt.ac.id/auth/sso/login', formData)
# # headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(jwt_get.json()['access'])}
# # http_get = requests.get('https://api.umkt.ac.id/managemen/mahasiswa/?kode_prodi=55201&angkatan=2021', headers=headers)
# formDataSikad = {'username': 'Haris', 'password': 'Haris', 'grant_type': 'password', 'client_id': 'web'}
# jwt_getSikad = requests.post('https://apiumkt.civitas.id/access_token', data=formDataSikad)
# headersSikad = {'Content-Type': 'application/json',
#                 'Authorization': 'Bearer {}'.format(jwt_getSikad.json()['access_token'])}
# http_get = requests.get('https://apiumkt.civitas.id/v1/mahasiswa?prodi=55201&angkatan=2021', headers=headersSikad)
# array = []
# for i in range(1, int(round(http_get.json()['meta']['totalItems'] / http_get.json()['meta']['itemsPerPage']))):
#     http_get = requests.get('https://apiumkt.civitas.id/v1/mahasiswa?prodi=55201&angkatan=2021&page={}'.format(i),
#                             headers=headersSikad)
#     array = array + http_get.json()['data']
# print(len(array))
#
#
# def getIpk(row):
#     http_get_ipk = requests.get(
#         'https://apiumkt.civitas.id/v1/mahasiswa/{}/khs?tahun={}&semester=4'.format(row['idMahasiswa'],
#                                                                                     datetime.today().year),
#         headers=headersSikad)
#     return http_get_ipk.json()['ipkSemesterSebelumnya']['ip']
#
#
# def getSks(row):
#     http_get_sks = requests.get(
#         'https://apiumkt.civitas.id/v1/mahasiswa/{}/khs?tahun={}&semester=4'.format(row['idMahasiswa'],
#                                                                                     datetime.today().year),
#         headers=headersSikad)
#     return http_get_sks.json()['kopLaporan']['sksTempuh']
#
#
# # print(http_get_ipk.json())
# # print(array)
# df = pd.DataFrame(array)
# # df.drop(['alamat', 'dosen', 'tempatLahir', 'tanggalLahir', 'telepon', 'noWa', ''],axis=1,inplace=True)
# df['prodi'] = df['prodi'][0]['idProdi']
# df['ipk'] = df.apply(getIpk, axis=1)
# df['sks'] = df.apply(getSks, axis=1)
# # with open('data.csv', 'w') as f:
# #     writer = csv.DictWriter(f, fieldnames=headerss)
# #     writer.writeheader()
# #     writer.writerows(http_get.json()['rows'])
# # print(df)
# # with open('data.csv', 'a') as file:
# df[['nama', 'idMahasiswa', 'prodi', 'ipk', 'sks']].to_csv('./data.csv')

import numpy as np


def ahp(matrix):
    # Step 1: Normalize the matrix
    normalized_matrix = matrix / matrix.sum(axis=0)

    # Step 2: Calculate the weighted matrix
    weights = normalized_matrix.mean(axis=1)

    # Step 3: Calculate the consistency ratio
    eigenvector = np.dot(normalized_matrix, weights)
    lambda_max = eigenvector.mean()
    consistency_index = (lambda_max - len(matrix)) / (len(matrix) - 1)

    # Consistency ratio threshold (adjust as needed)
    cr_threshold = 0.1

    if consistency_index < 0.1:
        print("Consistency Ratio:", consistency_index)
        print("Matrix is consistent.")
    else:
        print("Consistency Ratio:", consistency_index)
        print("Inconsistent matrix. Please review your judgments.")
        return

    return weights


# Example usage
criteria_matrix = np.array([
    [1, 3, 5],
    [1 / 3, 1, 3],
    [1 / 5, 1 / 3, 1]
])

criteria_weights = ahp(criteria_matrix)
print("Criteria Weights:", criteria_weights)