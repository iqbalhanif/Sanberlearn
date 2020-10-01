select
a.Title as Title
,b.Name as Name
,c.Name as Track
FROM tes.albums a
JOIN tes.artists b
ON a.ArtistId = b.ArtistId
JOIN tes.tracks c
ON a.AlbumId = c.AlbumId
WHERE b.Name = 'AC/DC'
AND a.Title = 'Let There Be Rock'
UNION
select
a.Title as Title
,b.Name as Name
,c.Name as Track
FROM tes.albums a
JOIN tes.artists b
ON a.ArtistId = b.ArtistId
JOIN tes.tracks c
ON a.AlbumId = c.AlbumId
WHERE b.Name = 'Aerosmith'
ORDER BY a.Title DESC;