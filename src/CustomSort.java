import java.util.ArrayList;

public class CustomSort implements SortingInterface {

    private ArrayList<Double> List;
    private int sorted = 0;

    @Override
    public void setValues(ArrayList<Double> values) {
        List = values;
        sort();
    }

    @Override
    public ArrayList<Integer> getGaps() {
        ArrayList<Integer> temp = new ArrayList<>();
        ArrayList<Integer> gaps = new ArrayList<>();
        int n = List.size();
        int gap = 1;
        int i = 2;
        while(gap < n) {
            temp.add(gap);
            gap = 2;
            for(int j = 0;j<i-1;j++){
                gap = gap*2;
            }
            gap = gap - 1;
            i++;
        }
        for (int k = temp.size() -1; k>=0; k--){
            gaps.add(temp.get(k));
        }
        return gaps;
    }

    @Override
    public void add(Double value) {
        if (sorted == 1){
            for (int i = 0; i<List.size();i++){
                if (value <= List.get(i)){
                    List.add(i,value);
                    return;
                }
            }
        }
        else{
            sort();
            for (int i = 0; i<List.size();i++){
                if (value <= List.get(i)){
                    List.add(i,value);
                    return;
                }
            }
        }
    }

    @Override
    public void remove(int index) {
        if (sorted == 1){
            List.remove(index);
        }
        else{
            sort();
            List.remove(index);
        }
    }

    @Override
    public void sort() {
        int n = List.size();
        ArrayList<Integer>gaps = getGaps();
        for (int gap : gaps){
            for (int i = gap; i <= n-1; i++){
                double temp = List.get(i);
                int j = 0;
                for (j = i; j>=gap; j -= gap){
                    if (List.get(j-gap) <= temp){
                        break;
                    }
                    List.set(j,List.get(j-gap));
                }
                List.set(j,temp);
            }
        }
        sorted = 1;
    }
}
