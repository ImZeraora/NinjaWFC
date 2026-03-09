document.addEventListener('DOMContentLoaded', function () {
  const groupsContainer = document.getElementById('groupsContainer');

  async function fetchRooms() {
    groupsContainer.innerHTML = '<div class="stats-status">Loading rooms...</div>';

    try {
      const response = await fetch('http://nas.ninjawfc.com/api/groups?game=mariokartwii');
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      renderRooms(data);
    } catch (error) {
      console.error('Error fetching data:', error);
      groupsContainer.innerHTML = '<div class="stats-status stats-error">Failed to load room data.</div>';
    }
  }

  function renderRooms(groups) {
    groupsContainer.innerHTML = '';

    if (!groups || groups.length === 0) {
      groupsContainer.innerHTML = '<div class="stats-status">No active rooms found.</div>';
      return;
    }

    groups.forEach(function (group) {
      const roomCard = document.createElement('div');
      roomCard.className = 'room-card';

      const createdDate = new Date(group.created);
      const roomOpenDuration = timeSince(createdDate);
      const rkLabel = getRkLabel(group.rk);
      const players = group.players || {};

      roomCard.innerHTML =
        '<h3 class="room-title">Room ID: ' + (group.id || 'Unknown') + '</h3>' +
        '<p><strong>Region (RK):</strong> ' + rkLabel + '</p>' +
        '<p><strong>Game:</strong> ' + (group.game || 'mariokartwii') + '</p>' +
        '<p><strong>Open for:</strong> ' + roomOpenDuration + '</p>' +
        '<p><strong>Players:</strong></p>';

      const playerEntries = Object.values(players);
      if (playerEntries.length === 0) {
        const noPlayers = document.createElement('div');
        noPlayers.className = 'room-player';
        noPlayers.textContent = 'No players in this room.';
        roomCard.appendChild(noPlayers);
      } else {
        playerEntries.forEach(function (player) {
          const playerDiv = document.createElement('div');
          playerDiv.className = 'room-player';
          playerDiv.innerHTML =
            '<p><strong>Name:</strong> ' + (player.name || 'Unknown') + '</p>' +
            '<p><strong>Friend Code:</strong> ' + (player.fc || 'Unknown') + '</p>' +
            '<p><strong>EV:</strong> ' + (player.ev || 'N/A') + ' | <strong>EB:</strong> ' + (player.eb || 'N/A') + '</p>';
          roomCard.appendChild(playerDiv);
        });
      }

      groupsContainer.appendChild(roomCard);
    });
  }

  function getRkLabel(rk) {
    if (rk === 'vs_20000' || rk === 'bt_20000') {
      return rk + " (Zeraora's Stream Essentials)";
    }
    if (rk === 'vs_20001' || rk === 'bt_20001') {
      return rk + ' (Mario Kart Mayhem)';
    }
    return rk || 'Unknown';
  }

  function timeSince(date) {
    const seconds = Math.floor((new Date() - date) / 1000);
    const minutes = Math.floor(seconds / 60);
    const hours = Math.floor(minutes / 60);

    if (hours > 0) {
      return hours + 'h ' + (minutes % 60) + 'm';
    }
    if (minutes > 0) {
      return minutes + 'm';
    }
    return seconds + 's';
  }

  fetchRooms();
  setInterval(fetchRooms, 60000);
});
