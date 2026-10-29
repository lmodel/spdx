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
  A collection of Elements, not necessarily with unifying context.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class ElementCollection extends Element {

  private List<Element> element;
  private List<String> profileConformance;
  private List<Element> rootElement;


}