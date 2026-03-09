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
      const createdDate = new Date(group.created);
      const roomOpenDuration = timeSince(createdDate);
      const rkLabel = getRkLabel(group.rk);
      const players = group.players || {};
      const gameValue = group.game || 'mariokartwii';
      const showGameRow = String(gameValue).toLowerCase() !== 'mariokartwii';
      const gameRowHtml = showGameRow
        ? '<tr>' +
          '<td class="label-cell">Game</td>' +
          '<td colspan="3">' + escapeHtml(gameValue) + '</td>' +
          '</tr>'
        : '';
      const roomTableWrapper = document.createElement('div');
      const roomTable = document.createElement('table');
      const playerEntries = Object.values(players);

      roomTableWrapper.className = 'room-table-wrapper';
      roomTable.className = 'room-table';
      roomTable.innerHTML =
        '<thead>' +
        '<tr><th colspan="4">Room ID: ' + escapeHtml(group.id || 'Unknown') + '</th></tr>' +
        '</thead>' +
        '<tbody>' +
        '<tr>' +
        '<td class="label-cell">Region (RK)</td>' +
        '<td colspan="3">' + escapeHtml(rkLabel) + '</td>' +
        '</tr>' +
        gameRowHtml +
        '<tr>' +
        '<td class="label-cell">Open For</td>' +
        '<td colspan="3">' + escapeHtml(roomOpenDuration) + '</td>' +
        '</tr>' +
        '<tr class="players-header-row">' +
        '<th>Player Name</th>' +
        '<th>Friend Code</th>' +
        '<th>EV</th>' +
        '<th>EB</th>' +
        '</tr>' +
        '</tbody>';

      if (playerEntries.length === 0) {
        const emptyRow = document.createElement('tr');
        emptyRow.className = 'no-players-row';
        emptyRow.innerHTML = '<td colspan="4">No players in this room.</td>';
        roomTable.querySelector('tbody').appendChild(emptyRow);
      } else {
        playerEntries.forEach(function (player) {
          const playerRow = document.createElement('tr');
          playerRow.innerHTML =
            '<td>' + escapeHtml(player.name || 'Unknown') + '</td>' +
            '<td>' + escapeHtml(player.fc || 'Unknown') + '</td>' +
            '<td>' + escapeHtml(player.ev || 'N/A') + '</td>' +
            '<td>' + escapeHtml(player.eb || 'N/A') + '</td>';
          roomTable.querySelector('tbody').appendChild(playerRow);
        });
      }

      roomTableWrapper.appendChild(roomTable);
      groupsContainer.appendChild(roomTableWrapper);
    });
  }

  function escapeHtml(value) {
    return String(value)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
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
