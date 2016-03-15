import java.util.Random;

public class GenGroup
{
  public static void main(String args[])
  {
     Random r=new Random();
     int theatreCapacity=0,numGroups=0;
     if (args==null || args.length<2)
     {
       System.err.println("Proper usage is java GenGroup <theatre capacity> <number of groups>");
       System.exit(0);
     }

     try 
     {
       theatreCapacity=Integer.parseInt(args[0]);
       numGroups=Integer.parseInt(args[1]);
       if (theatreCapacity<=0 || numGroups<=0)
         throw new NumberFormatException();
     } catch (NumberFormatException nfe) 
     {
       System.err.println("Theatre capacity and number of groups must be an integer greater than 0");
       System.exit(0);
     }

     for (int i=0;i<numGroups;i++)
     {
       int rand=1+r.nextInt(theatreCapacity);
       System.out.println(rand);
     }

  }
}
