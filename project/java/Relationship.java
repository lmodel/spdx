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
  Describes a relationship between one or more elements.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Relationship extends Element {

  private String completeness;
  private ZonedDateTime endTime;
  private Element from;
  private String relationshipType;
  private ZonedDateTime startTime;
  private List<Element> to;


}