package example;

/* metamodel_version: 1.12.0 */
/* version: 3.0.1 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A characterization of some aspect of an Element that is associated with the Element in a generalized fashion.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class Extension  {

  private String type;


}