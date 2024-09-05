class Indamon {
    private String name;
    private int hp;
    private int attack;
    private int defense;
    private boolean fainted;
    
    public Indamon(String name, int hp, int attack, int defense) {
        this.name = name;
        this.hp = hp;
        this.attack = attack;
        this.defense = defense;
        fainted = false;
    }
    
    // getters
    public String getName() { return name; }
    public int getHp() { return hp; }
    public int getAttack() { return attack; }
    public int getDefense() { return defense; }
    public boolean getFainted() { return fainted; }

    // setters
    public void setName(String name) { this.name = name; }
    public void setHp(int hp) { this.hp = hp; }
    public void setAttack(int attack) { this.attack = attack; }
    public void setDefense(int defense) { this.defense = defense; }
    public void setFainted(boolean fainted) { this.fainted = fainted;}

    // attack method
    public void attackOponnent(Indamon target) {
        int damage = attack / target.getDefense();
        target.setHp(target.getHp() - damage);
        if (target.getHp() <= 0) {
            target.setFainted(true);
        }
    }

    // print info method
    public void printInfo() {
        System.out.println("Name: " + name);
        System.out.println("HP: " + hp);
        System.out.println("Attack: " + attack);
        System.out.println("Defense: " + defense);
        System.out.println("Fainted: " + fainted);
    }   
    
    public static void main(String[] args) {
        // create a new "Indamon" object
        Indamon glassey = new Indamon("Glassey", 10, 5, 5);
        Indamon siberov = new Indamon("Siberov", 10, 5, 5);
        // print out the object's info
        glassey.printInfo();
        siberov.printInfo();
        // call the attack method
        glassey.attack(siberov);
        siberov.printInfo();
    } // end main method
}
