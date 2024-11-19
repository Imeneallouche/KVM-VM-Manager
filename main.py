import libvirt
import sys


def print_menu():
    """Displays the main menu."""
    print("\nProgramme de gestion des machines virtuelles :")
    print("0) Nom de la machine hyperviseur")
    print("1) Lister les machines virtuelles")
    print("2) Démarrer une machine virtuelle")
    print("3) Arrêter une machine virtuelle")
    print("4) Afficher l'adresse IP d'une machine virtuelle")
    print("5) Quitter")
    print("Votre choix : ", end="")


def list_virtual_machines(conn):
    """Lists all defined (not running) and running virtual machines."""
    print("\nMachines virtuelles définies (non en cours d'exécution) :")
    for name in conn.listDefinedDomains():
        print(f"- {name}")

    print("\nMachines virtuelles en cours d'exécution :")
    for id in conn.listDomainsID():
        dom = conn.lookupByID(id)
        print(f"- {dom.name()} (ID: {id})")


def start_virtual_machine(conn):
    """Starts a selected virtual machine."""
    vms = conn.listDefinedDomains()
    if not vms:
        print("Aucune machine virtuelle définie à démarrer.")
        return

    print("\nChoisissez une machine virtuelle à démarrer :")
    for index, name in enumerate(vms):
        print(f"{index}) {name}")

    choice = int(input("Votre choix : "))
    if 0 <= choice < len(vms):
        dom = conn.lookupByName(vms[choice])
        dom.create()
        print(f"Machine virtuelle '{vms[choice]}' démarrée avec succès.")
    else:
        print("Choix invalide.")


def stop_virtual_machine(conn):
    """Stops a selected running virtual machine."""
    ids = conn.listDomainsID()
    if not ids:
        print("Aucune machine virtuelle en cours d'exécution à arrêter.")
        return

    print("\nChoisissez une machine virtuelle à arrêter :")
    for index, id in enumerate(ids):
        dom = conn.lookupByID(id)
        print(f"{index}) {dom.name()} (ID: {id})")

    choice = int(input("Votre choix : "))
    if 0 <= choice < len(ids):
        dom = conn.lookupByID(ids[choice])
        dom.destroy()  # Use `dom.shutdown()` for a graceful shutdown
        print(f"Machine virtuelle '{dom.name()}' arrêtée avec succès.")
    else:
        print("Choix invalide.")


def get_vm_ip_address(conn):
    """Retrieves the IP address of a running virtual machine using libvirt."""
    vm_name = input("Entrez le nom de la machine virtuelle : ")
    try:
        dom = conn.lookupByName(vm_name)
        if dom is None:
            print(f"Machine virtuelle '{vm_name}' introuvable.")
            return

        # Ensure the VM is running
        if dom.isActive() != 1:
            print(f"Machine virtuelle '{vm_name}' n'est pas en cours d'exécution.")
            return

        # Get the IP address
        interfaces = dom.interfaceAddresses(
            libvirt.VIR_DOMAIN_INTERFACE_ADDRESSES_SRC_AGENT, 0
        )
        for interface_name, interface_data in interfaces.items():
            if interface_data["addrs"]:
                for addr in interface_data["addrs"]:
                    if addr["type"] == libvirt.VIR_IP_ADDR_TYPE_IPV4:
                        print(
                            f"Adresse IP de '{vm_name}' sur l'interface '{interface_name}': {addr['addr']}"
                        )
                        return

        print(
            f"Aucune adresse IP trouvée pour '{vm_name}'. Assurez-vous que 'qemu-guest-agent' est installé et en cours d'exécution dans la VM."
        )
    except libvirt.libvirtError as e:
        print(f"Erreur lors de la récupération de l'adresse IP : {e}")


def main():
    """Main function to run the interactive menu."""
    try:
        conn = libvirt.open("qemu:///system")
        if conn is None:
            print("Impossible de se connecter à l'hyperviseur.")
            sys.exit(1)

        while True:
            print_menu()
            choice = input()

            if choice == "0":
                print(f"Nom de la machine hyperviseur : {conn.getHostname()}")
            elif choice == "1":
                list_virtual_machines(conn)
            elif choice == "2":
                start_virtual_machine(conn)
            elif choice == "3":
                stop_virtual_machine(conn)
            elif choice == "4":
                get_vm_ip_address(conn)
            elif choice == "5":
                print("Quitter le programme.")
                break
            else:
                print("Choix invalide. Veuillez essayer à nouveau.")

        conn.close()
    except libvirt.libvirtError as e:
        print(f"Erreur Libvirt : {e}")
    except ValueError:
        print("Entrée invalide. Veuillez entrer un nombre.")


if __name__ == "__main__":
    main()
