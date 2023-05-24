package interview.mntn;

/**
 * There is a list of cities you have the option of moving to, but you haven't decided which one.
 * All cities are equally appealing, and the only factor you have not considered yet is average temperature.
 * You prefer moderate climates, so you want to find the city in the list with the most median temperature.
 * Given a singly linked list, find the optimal city.
 * Next, make another function that will find the city with the average temperature closest to a temperature passed as a parameter.
 */

class Main {

    public static String getMedianCity(CityNode head) {
        CityNode singleNode = head;
        CityNode doubleNode = head;

        while (doubleNode.next != null) {
            singleNode = singleNode.next;
            doubleNode = doubleNode.next;
            if (doubleNode.next != null) {
                doubleNode = doubleNode.next;
            } else {
                break;
            }
        }

        return singleNode.city.getName();
    }

    public static String getIdealCity(CityNode head, int idealTemp) {
        CityNode previous = head;
        CityNode current = head;

        while (current.city.getTemperature() >= idealTemp && current.next != null) {
            previous = current;
            current = current.next;
        }

        if (Math.abs(idealTemp - current.city.getTemperature()) < Math.abs(idealTemp - previous.city.getTemperature())) {
            return current.city.getName();
        } else {
            return previous.city.getName();
        }
    }

    public static void main(String[] args) {
        CityNode minneapolis = new CityNode(new City("Minneapolis", 55), null);
        CityNode chicago = new CityNode(new City("Chicago", 60), minneapolis);
        CityNode seattle = new CityNode(new City("Seattle", 68), chicago);
        CityNode sanJose = new CityNode(new City("San Jose", 74), seattle);
        CityNode raleigh = new CityNode(new City("Raleigh", 79), sanJose);
        CityNode atlanta = new CityNode(new City("Atlanta", 81), raleigh);
        CityNode phoenix = new CityNode(new City("Phoenix", 86), atlanta);
        CityNode houston = new CityNode(new City("Houston", 88), phoenix);

        System.out.println(getMedianCity(houston));
        System.out.println(getMedianCity(phoenix));
        System.out.println(getIdealCity(houston, 50));
        System.out.println(getIdealCity(houston, 68));
        System.out.println(getIdealCity(houston, 80));
        assert getMedianCity(houston).equals(sanJose.city.getName());
        assert getMedianCity(phoenix).equals(sanJose.city.getName());
        assert getIdealCity(houston, 50).equals(minneapolis.city.getName());
        assert getIdealCity(houston, 68).equals(seattle.city.getName());
        assert getIdealCity(houston, 80).equals(atlanta.city.getName());
    }
}

class City {
    private String name;
    private int temperature;

    public City(String name, int temperature) {
        this.name = name;
        this.temperature = temperature;
    }

    public int getTemperature() {
        return temperature;
    }

    public String getName() {
        return name;
    }
}

class CityNode {
    public City city;
    public CityNode next;

    public CityNode(City city, CityNode next) {
        this.city = city;
        this.next = next;
    }
}
