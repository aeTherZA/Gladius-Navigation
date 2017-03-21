/**
 * Created by darrenadams on 2017/03/21.
 */
public class GPSObject {
    private GPSCoords coordinates;

    public GPSObject()
    {
        coordinates = new GPSCoords();
    }

    /**
     * Get's coordinates of location.
     * @param n Name of the location
     * @return object holding location's coordinates
     */
    public GPSObject getCoords(String n)
    {
        //Create GISRequest
        GISRequest req = new GISRequest(n);
        GISDataObject obj = GISDataObject::getGISDataObject(req);
        this.coordinates.set(obj);

        return this;
    }
}

class GPSCoords{
    private float longlat[];


    public GPSCoords()
    {
        longlat = new float[2];
    }

    /**
     * Sets longlat to coordinates in GISDataObject
     * @param obj GIS Module returned data
     *
     */
    public void set(GISDataObject obj)
    {

        this.longlat = obj.GPSCoord;
    }

}
