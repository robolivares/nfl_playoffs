from firebase_functions import firestore_fn
from firebase_admin import initialize_app, firestore

initialize_app()

POINTS_PER_ROUND = {'wc': 3, 'div': 5, 'conf': 8, 'super': 13}

@firestore_fn.on_document_written(document="tournaments/{tournId}/results/actualResults")
def on_results_update(event: firestore_fn.Event[firestore_fn.Change]) -> None:
    tourn_id = event.params["tournId"]
    db = firestore.client()

    # 1. Get official winners from admin.html
    actual_data = event.data.after.to_dict() or {}
    actual_winners = actual_data.get('winners', {})

    # 2. Get all player brackets from index.html collection
    # We changed 'participants' to 'entries' to match your HTML
    entries = db.collection('tournaments', tourn_id, 'entries').stream()

    leaderboard = []

    for doc in entries:
        p = doc.to_dict()
        picks = p.get('picks', {})

        score = 0
        for game_id, picked_team in picks.items():
            if game_id in actual_winners:
                if picked_team == actual_winners[game_id]:
                    # Identify points by the game ID (e.g., 'afc_wc_1')
                    if 'wc' in game_id: score += POINTS_PER_ROUND['wc']
                    elif 'div' in game_id: score += POINTS_PER_ROUND['div']
                    elif 'champ' in game_id: score += POINTS_PER_ROUND['conf']
                    elif 'super' in game_id: score += POINTS_PER_ROUND['super']

        leaderboard.append({
            "name": p.get('name', 'Anonymous'),
            "score": score
        })

    # 3. Sort and save for the UI to read
    leaderboard.sort(key=lambda x: x['score'], reverse=True)

    db.collection('tournaments', tourn_id, 'state').document('viewerData').set({
        "participants": leaderboard,
        "lastUpdated": firestore.SERVER_TIMESTAMP
    })
