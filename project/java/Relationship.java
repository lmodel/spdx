package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.1 */
import java.util.List;
import lombok.*;

/**
  Describes a relationship between one or more elements.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Relationship extends Element {

  private List<Element> to;
  private String completeness;
  private ZonedDateTime startTime;
  private String relationshipType;
  private Element from;
  private ZonedDateTime endTime;

}