package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.1 */
import java.util.List;
import lombok.*;

/**
  Provides information about the creation of the Element.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CreationInfo  {

  private List<Agent> createdBy;
  private List<Tool> createdUsing;
  private ZonedDateTime created;
  private String specVersion;
  private String comment;

}