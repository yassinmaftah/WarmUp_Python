# Créer les tables dans PostgreSQL en utilisant SQLAlchemy.
# Insérer les données fournies ci-dessus.
# Lister tous les plats triés par prix décroissant.
from sqlalchemy import select, desc, or_

stmt1 = select(Plat).order_by(desc(Plat.prix))
plats_desc = session.execute(stmt1).scalars().all()

for p in plats_desc:
    print(f"{p.nom} | {p.prix} dh")
# Lister tous les plats dont le prix est compris entre 30 et 80.
stmt2 = select(Plat).where(Plat.prix.between(30, 80))
plats_30_80 = session.execute(stmt2).scalars().all()

for p in plats_30_80:
    print(f"{p.nom} | {p.prix} MAD")
# Afficher les clients dont le nom commence par "S" ou "F".
stmt3 = select(Client).where(
    or_(
        Client.nom.startswith('S'),
        Client.nom.startswith('F')
    )
)
clients_sf = session.execute(stmt3).scalars().all()

for c in clients_sf:
    print(f"{c.nom}")

# Afficher les plats avec leur nom de catégorie et le nom du fournisseur principal (via l'ingrédient le plus utilisé).
# Lister les commandes avec le nom du client, la date, et le nombre total de plats commandés.
from sqlalchemy import select,func
s = select(
    Commande.id,Client.nom,Commande.date_command,
    func.sum(CommandePlat.quantite).label('total_plats')
).join(Client, Client.id == Commande.client_id)\
.join(CommandePlat, Commande.id == CommandePlat.commande_id)
.groupby(Commande.id,Client.nom,Commande.date_command)\
.order_by(Commande.id)
result00 = session.execute(s)

for cmd_id, nom_client, date_cmd, total_plats in commandes_infos:
    date_propre = date_cmd.strftime('%Y-%m-%d')
    print(f"Commande #{cmd_id} | {nom_client:<15} | {date_propre} | {total_plats} plats") 



# Pour chaque commande, afficher les plats commandés, leur quantité, et le coût total des ingrédients.
# Afficher le nombre de plats pour chaque catégorie, y compris celles sans plats.
# Afficher le prix moyen des plats par catégorie et le coût moyen des ingrédients par plat.
# Afficher le nombre de commandes par client, trié par ordre décroissant.
# Afficher les clients ayant passé plus de deux commandes.
# Lister les plats commandés plus de trois fois avec leur total de quantités et leur note moyenne (via avis).
# Lister les commandes du troisième trimestre 2025 (juillet à septembre).
# Afficher la commande la plus récente avec le nom du client et les plats commandés.
# Afficher les clients ayant passé une commande d’un montant supérieur à 150, avec leur numéro de téléphone.
# Afficher les plats dont le coût total des ingrédients est supérieur à 50% du prix du plat.
# Ajouter un nouveau plat dans la catégorie "Végétarien" avec deux ingrédients.
# Supprimer le client "Youssef El Khalfi", ses commandes, et ses avis.
# Afficher pour chaque client :
# Son nom
# Le nombre total de plats commandés
# Le montant total dépensé
# La note moyenne de leurs avis
# Lister les 3 plats les plus commandés (par quantité totale) avec leur catégorie.
# Afficher les clients et leurs dernières commandes, incluant les plats commandés.
# Créer une vue virtuelle (SELECT) qui affiche :
# Le nom du client
# Les plats commandés
# Les quantités
# La date de la commande
# La note moyenne du plat (via avis)
# Afficher les fournisseurs dont les ingrédients sont en stock inférieur à 10 unités, avec le coût total des ingrédients en stock.
