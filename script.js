document.addEventListener('DOMContentLoaded', function() {
  const groupsContainer = document.getElementById('groupsContainer');

  fetch('http://ninjawfc.com/api/groups?game=mariokartwii')
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      data.forEach(group => {
        const groupTable = createGroupTable(group);
        groupsContainer.appendChild(groupTable);
      });
    })
    .catch(error => {
      console.error('Error fetching data:', error);
    });

  function createGroupTable(groupData) {
    const groupTable = document.createElement('table');
    groupTable.classList.add('table', 'table-striped', 'mb-5');

    // Table header for group info
    const groupInfoHeader = document.createElement('thead');
    groupInfoHeader.innerHTML = `
      <tr>
        <th colspan="2">Group Info</th>
      </tr>
    `;
    groupTable.appendChild(groupInfoHeader);

    // Table body for group info
    const groupInfoBody = document.createElement('tbody');
    groupInfoBody.innerHTML = `
      <tr>
        <td>Tag:</td>
        <td>${groupData.id}</td>
      </tr>
      <tr>
        <td>Type:</td>
        <td>${groupData.type}</td>
      </tr>
      <tr>
        <td>Created:</td>
        <td>${formatDate(groupData.created)}</td>
      </tr>
      <tr>
        <td>Host:</td>
        <td>${getPlayerName(groupData.host, groupData.players)}</td>
      </tr>
      <tr>
        <td>Gamemode:</td>
        <td>${groupData.rk}</td>
      </tr>
    `;
    groupTable.appendChild(groupInfoBody);

    // Separate row for player headers
    const playersHeader = document.createElement('thead');
    playersHeader.innerHTML = `
      <tr>
        <th>Name</th>
        <th>Friend Code</th>
        <th>VR</th>
        <th>BR</th>
      </tr>
    `;
    groupTable.appendChild(playersHeader);

    // Table body for players
    const playersBody = document.createElement('tbody');
    Object.values(groupData.players).forEach(player => {
      const row = document.createElement('tr');
      row.innerHTML = `
        <td>${player.name}</td>
        <td>${player.fc}</td>
        <td>${player.ev}</td>
        <td>${player.eb}</td>
      `;
      playersBody.appendChild(row);
    });
    groupTable.appendChild(playersBody);

    return groupTable;
  }

  function getPlayerName(hostId, players) {
    const hostPlayer = players[hostId];
    return hostPlayer ? hostPlayer.name : 'Unknown';
  }

  function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleString();
  }
});
