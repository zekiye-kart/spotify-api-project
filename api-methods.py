def get_access_token(client_id, client_secret):
    
        """
    Token alır

    Params:

    client_id: spotify client id
    client_secret:  spotify client secret
    
    Returns:
    acces token
    
    """
    # Spotify API'ye yetkilendirme bilgilerini base64 ile kodla
    client_credentials = f"{client_id}:{client_secret}"
    client_credentials_b64 = base64.b64encode(client_credentials.encode()).decode()

    # Yetkilendirme isteği yap
    url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization': f'Basic {client_credentials_b64}',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {'grant_type': 'client_credentials'}

    response = requests.post(url, headers=headers, data=data)
    access_token = response.json().get('access_token')

    return access_token




def get_artist_top_tracks(artist_id, access_token):
       """
    Belirlenen sanatçının bilgilerini alır

    Params:

    artist_id: spotify daki sanatçının id si
    access_token:  erişim
    
    Returns: json dosyası
    
    """
    url = f'https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=TR'
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(url, headers=headers)
    return response.json()




def get_artist_albums(artist_id, access_token):
    
           """
    Belirlenen sanatçının albümlerini alır

    Params:
    artist_id: spotify daki sanatçının id si
    access_token:  erişim
    
    Returns: json dosyası
    
    """
    
    url = f'https://api.spotify.com/v1/artists/{artist_id}/albums'
    headers = {'Authorization': f'Bearer {access_token}'}
    artistalbum_response = requests.get(url, headers=headers)
    return  artistalbum_response.json()





def get_album_tracks(album_id, access_token):
               """
    Belirlenen sanatçının albümlerindeki parçaları alır

    Params:
    artist_id: spotify daki sanatçının id si
    access_token:  erişim
    
    Returns: json dosyası
    
    """
    url = f'https://api.spotify.com/v1/albums/{album_id}/tracks'
    headers = {'Authorization': f'Bearer {access_token}'}
    albumtrack_response = requests.get(url, headers=headers)
    return albumtrack_response.json()







