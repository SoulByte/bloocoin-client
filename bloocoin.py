import cmd
import os
import coins
import addr
import register
import send
import transactions
import total_coins
import check_addr

__version__ = 0.03


class BlooClient(cmd.Cmd):
    prompt = "BlooCoin$ "
    intro = "The BlooCoin Official Client version " + str(__version__) + "\nType help for a list of commands\n"

    def do_coins(self, line):
        print coins.coins()

    def do_addr(self, line):
        print addr.addr()

    def do_send(self, line):
        line = line.split()
        amt = int(line[0])
        to = line[1]
        print send.send(amt, to)

    def do_transactions(self, line):
        transactions.transactions()

    def do_totalcoins(self, line):
        print "There are "+str(total_coins.total_coins())+" coins in circulation."
    
    def do_checkaddr(self, line):
        line = line.split()
        addr = line[0]
        print check_addr.check_addr(addr)
        
    def do_help(self, line):
        print """

        BlooCoin Client Commands

        send <amt> <addr> - Send coins to an address.
        coins - Shows the amount of coins that you have.
        addr - Shows your BLC address.
        transactions - Shows all transactions you have made.
        totalcoins - Shows all coins in curculation.
        checkaddr <addr> - Checks how many coins belong to a specific address.
        help - Displays this prompt.

        """
if __name__ == "__main__":
    if not os.path.exists("bloostamp"):
        register.register()
    BlooClient().cmdloop()
