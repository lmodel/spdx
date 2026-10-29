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
  Provides information about the creation of the Element.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CreationInfo  {

  private String type;
  private String comment;
  private String created;
  private List<Agent> createdBy;
  private List<Tool> createdUsing;
  private String specVersion;


}